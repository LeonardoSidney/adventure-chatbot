import uvicorn
import uvicorn.server
from adventure_chatbot import Main, ArgsHelper, Server

argsHelper = ArgsHelper()
args = argsHelper.getArgs()

def start_console():
    main = Main()
    main.execute()

server = Server(args)
server.execute()
app = server.http

if __name__ == "__main__":
    config = uvicorn.Config(app, host=args.host, port=args.port)
    if args.reload:
        config = uvicorn.Config("server:app", host=args.host, port=args.port, reload=args.reload)

    uvsrv = uvicorn.Server(config)
    uvsrv.run()
    # start_console()