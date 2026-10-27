exports.handler = async (event) => {
    try {
        const body = JSON.parse(event.body || '{}');
        const { provider, token } = body;

        if (!provider || !token) {
            return {
                statusCode: 400,
                headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
                body: JSON.stringify({ message: "Provedor e token são obrigatórios." })
            };
        }

        const mockUser = {
            id: "user_12345",
            email: "usuario@exemplo.com",
            name: "Usuário Exemplo",
            provider: provider
        };

        return {
            statusCode: 200,
            headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
            body: JSON.stringify({
                message: "Autenticação realizada com sucesso.",
                accessToken: "jwt_session_token_sample",
                user: mockUser
            })
        };
    } catch (error) {
        return {
            statusCode: 500,
            headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
            body: JSON.stringify({ message: "Erro interno no servidor.", error: error.message })
        };
    }
};