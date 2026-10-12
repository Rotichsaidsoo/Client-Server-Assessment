# Local Client-Server Application (VS Code)

## Requirements
- Python 3 installed
- Visual Studio Code

## Run it
1. Extract the ZIP file.
2. Open VS Code and select **File > Open Folder**, then select `client_server_assessment`.
3. Select **Terminal > New Terminal**.
4. Check Python is installed with `py --version` on Windows (or `python3 --version` on macOS/Linux).
5. Start the server:
   - Windows: `py server.py`
   - macOS/Linux: `python3 server.py`
6. In your browser, open **http://127.0.0.1:8000**
7. Type `Hello server!` and click **Send message**. The page should show **HTTP communication successful (200 OK)** and the server reply.
8. Keep the terminal open while testing. Stop the server with `Ctrl+C`.

## Assessment demonstration
- The browser page is the client interface.
- The VS Code terminal shows the server running and logs each client request.
- The page shows the response sent by the server.
- The architecture section identifies the presentation, client, server, and transport/network layers.

## Important about the link
`http://127.0.0.1:8000` is a localhost address and works only on the computer running the server. It is not a public link that your lecturer can open remotely. Submit the ZIP file and screenshots/video of the running application, or deploy it to a hosting service if a public URL is required.
