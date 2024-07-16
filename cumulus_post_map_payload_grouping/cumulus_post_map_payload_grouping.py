def lambda_handler(event, context):
    fail_count = 0
    for e in event:
        print(e.get('Status'))
        if e.get('Status') == 'FAILED':
            fail_count = fail_count + 1

    if fail_count > 0:
        raise Exception(f'Map has counted failed unpacks (total: {fail_count}')

    return {
        'statusCode': 200,
        'body': {
            "total_count": len(event),
            "fail_count": fail_count
        }
    }
