const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, PutCommand, GetCommand } = require("@aws-sdk/lib-dynamodb");

// Configuração flexível: Funciona localmente (Docker) e na Nuvem AWS
const clientConfig = {
    region: process.env.AWS_REGION || "sa-east-1",
};

// Se existir endpoint local no env.json, aponta para o Docker (local); se não, usa a nuvem
if (process.env.DYNAMODB_ENDPOINT) {
    clientConfig.endpoint = process.env.DYNAMODB_ENDPOINT;
    clientConfig.credentials = {
        accessKeyId: "local",
        secretAccessKey: "local"
    };
}

const client = new DynamoDBClient(clientConfig);
const docClient = DynamoDBDocumentClient.from(client);
const TABLE_NAME = process.env.TABLE_NAME || "users";

exports.handler = async (event, context) => {
    // Configuração de CORS para permitir que a interface Web acesse a API
    const headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type,Authorization",
        "Access-Control-Allow-Methods": "POST,OPTIONS"
    };

    const httpMethod = event.requestContext?.http?.method || event.httpMethod;
    if (httpMethod === "OPTIONS") {
        return { statusCode: 200, headers, body: "" };
    }

    try {
        const body = typeof event.body === "string" ? JSON.parse(event.body || "{}") : (event.body || {});
        const { email, name, provider, providerId } = body;

        if (!email || !providerId) {
            return {
                statusCode: 400,
                headers,
                body: JSON.stringify({ message: "email e providerId são obrigatórios." })
            };
        }

        // Procura usuário existente
        const getResult = await docClient.send(
            new GetCommand({
                TableName: TABLE_NAME,
                Key: { providerId }
            })
        );

        let user = getResult.Item;

        // Se for o primeiro acesso, cria no DynamoDB
        if (!user) {
            user = {
                providerId,
                email,
                name: name || "Usuário",
                provider: provider || "external",
                role: "user",
                createdAt: new Date().toISOString(),
                updatedAt: new Date().toISOString()
            };

            await docClient.send(
                new PutCommand({
                    TableName: TABLE_NAME,
                    Item: user
                })
            );
        }

        return {
            statusCode: 200,
            headers,
            body: JSON.stringify({
                message: "Autenticação realizada com sucesso",
                user: {
                    providerId: user.providerId,
                    name: user.name,
                    email: user.email,
                    role: user.role
                }
            })
        };
    } catch (error) {
        console.error("Erro interno:", error);
        return {
            statusCode: 500,
            headers,
            body: JSON.stringify({ error: "Erro interno no servidor ao acessar o banco de dados." })
        };
    }
};