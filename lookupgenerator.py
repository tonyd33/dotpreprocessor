#!/usr/bin/python
def main():
    from lookup import lookup
    import json
    with open("lookup.json", "w") as file:
        json.dump(lookup, file, indent=2)

if __name__ == '__main__':
    main()
