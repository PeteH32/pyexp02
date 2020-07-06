resource "aws_kinesis_stream" "stream_peteh01" {
  name             = "peteh01"
  shard_count      = 1
  retention_period = 24

  tags = {
    Environment      = "CodeChallenge_01"
    Creator          = "Pete-Heirendt"
    TerraformCreated = 1
  }
}
