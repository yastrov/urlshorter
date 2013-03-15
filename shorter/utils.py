import base64

def b64ToInt(uri):
    """Int in Base64 format to int"""
    return int(base64.b64decode(uri))

def intToB64(uri):
    """Int to int in Base64 format"""
    return base64.b64encode(str(uri))