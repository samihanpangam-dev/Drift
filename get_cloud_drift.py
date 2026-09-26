def get_cloud_drift():
    """Returns the manual changes detected in the cloud."""
    return {
        "resource": "aws_instance.api_server",
        "changed_attribute": "instance_type",
        "old_value": "t2.micro",
        "new_value": "t2.large",
        "timestamp": "2026-09-26T03:00:00Z",
        "user": "tired_senior_engineer"
    }