```sh
export IAM_USER="iam-user"

aws iam put-user-policy `
>>   --user-name user1 `    
>>   --policy-name route53-rr-role `
>>   --policy-document file://assume.policy.json
``` 