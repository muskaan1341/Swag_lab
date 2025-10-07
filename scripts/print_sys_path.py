import sys, json
print(json.dumps(sys.path, indent=2))
print('CWD:', __import__('os').getcwd())
