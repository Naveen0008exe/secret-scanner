def reporter(filepath , findings ):
    if not findings:
        print(f"we are clean {filepath} ")
        return
    
    print(f"\n{'*'*50}")
    print(f"we found something : {filepath}")
    print(f"\n{'*'*50}")

    for find in findings:
        print(f"\n  Type     : {find['type']}")
        print(f"  Method   : {find['method']}")
        print(f"  Line     : {find['line_number']}")
        print(f"  Content  : {find['line']}")
        print(f"  Severity : {'## CRITICAL' if find['type'] == 'AWS Key' else '*# HIGH'}")
    

    print(f"\n{'*'*60}")