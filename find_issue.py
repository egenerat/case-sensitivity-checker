

def find_suspects(calling_references, existing_static_files):
    for ref in calling_references:
        if ref not in existing_static_files:
            print(ref)
