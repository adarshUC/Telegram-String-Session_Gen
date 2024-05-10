from pyrogram import Client
def genStrSession():
    with Client(
        "ad",
        api_id= int(input("Enter Telegram APP ID: ")),
        api_hash= input("Enter Telegram API HASH: "),
        ) as app:
        print("\nprocessing...")
        app.send_message(
            "me", f"#STRING_SESSION by @NoobAadarsh\n\n```{app.export_session_string()}```"
        )
        print("Done !, session string has been sent to saved messages!")
genStrSession()