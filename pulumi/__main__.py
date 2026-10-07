"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
# from pulumi_aws import s3

# # Create an AWS resource (S3 Bucket)
# bucket = s3.Bucket('my-bucket')

# # Export the name of the bucket
# pulumi.export('bucket_name', bucket.id)

if pulumi.get_stack() == "prod":
    aws.route53.Zone("negoci-online", name="negoci.online")