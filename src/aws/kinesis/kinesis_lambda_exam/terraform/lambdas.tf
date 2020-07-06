////////////////////////////////////////////////////////////////////////////////
// Lambda: Producer
resource "aws_lambda_function" "cc_producer" {
  filename      = "lambda_producer_files.zip"
  function_name = "lambda_producer"
  handler       = "lambda_producer.handler_producer"
  role          = aws_iam_role.iam_for_lambdas.arn
  runtime       = "python3.7"

  environment {
    variables = {
      stream_name = aws_kinesis_stream.stream_peteh01.name
    }
  }

  tags = {
    Environment      = "CodeChallenge_01"
    Creator          = "Pete-Heirendt"
    TerraformCreated = 1
  }
}

////////////////////////////////////////////////////////////////////////////////
// Lambda: Consumer
// TODO


////////////////////////////////////////////////////////////////////////////////
// Lambda IAM roles/policies

resource "aws_iam_role" "iam_for_lambdas" {
  name = "iam_for_lambdas"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF

  tags = {
    Environment      = "CodeChallenge_01"
    Creator          = "Pete-Heirendt"
    TerraformCreated = 1
  }
}

// Needed so the lambda can put/get into the Kinesis streams
resource "aws_iam_policy" "policy_kinesis_access" {
  name        = "access-kinesis-streams"
  description = "Allow access to Kinesis streams"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "kinesis:PutRecord",
        "kinesis:PutRecords",
        "kinesis:GetShardIterator",
        "kinesis:GetRecords"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}

// Needed so the lambda can put/get into the Kinesis streams
resource "aws_iam_role_policy_attachment" "attach-lambda-kinesis-access" {
  role       = aws_iam_role.iam_for_lambdas.name
  policy_arn = aws_iam_policy.policy_kinesis_access.arn
}

// Needed so the lambda can log to CloudWatch
resource "aws_iam_role_policy_attachment" "attach-lambda-basic-role" {
  role       = aws_iam_role.iam_for_lambdas.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

