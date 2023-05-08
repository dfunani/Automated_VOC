from sys import argv
import asyncio
async def strapi(id: int):
    microapp = MicroApps()
    if not id:
        return
    new_app = microapp.fetchOne(id)
    print(new_app)
    print(new_app.get('result', {}))
        

if __name__ == "__main__":
    from admin.api import MicroApps
    if len(argv) != 1:
        asyncio.run(strapi(int(argv[1])))
else:
    from .admin.api import MicroApps
