from sys import argv

def strapi(id: int):
    microapp = MicroApps()
    if not id or type(id) is not int:
        return {"status": 'Invalid ID provided', 'result': 'ID must be integer'}
    return microapp.fetchOne(id)
        

if __name__ == "__main__":
    from admin.api import MicroApps
    if len(argv) != 1:
        strapi(int(argv[1]))
else:
    from .admin.api import MicroApps
