def lambda_handler(event, context):
    fail_count = 0
    for e in event.get('cma').get('event'):
        cumulus_meta = e.get('cumulus_meta')
        print(e.get('result'))
        if e.get('result') != 'success':
            fail_count = fail_count + 1

    if fail_count > 0:
        raise Exception(f'Map has counted failed unpacks (total: {fail_count})')

    return {
        'cumulus_meta': cumulus_meta,
        'statusCode': 200,
        'body': {
            "total_count": len(event),
            "fail_count": fail_count
        }
    }
