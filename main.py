# # from fastapi import FastAPI, Form, Request
# # from fastapi.responses import JSONResponse
# # import smtplib
# # from email.message import EmailMessage
# # import json
# # import datetime

# # app = FastAPI(title="Multi-SMTP Mail Sender API")

# # # Load cấu hình SMTP
# # with open("smtp_config.json", "r") as f:
# #     SMTP_CONFIGS = json.load(f)

# # # Dữ liệu đếm số lần gửi (lưu tạm trong RAM)
# # daily_sent_counter = {key: 0 for key in SMTP_CONFIGS.keys()}

# # def send_email(subject, body, to_email, smtp_conf):
# #     msg = EmailMessage()
# #     msg["Subject"] = subject
# #     msg["From"] = smtp_conf["user"]
# #     msg["To"] = to_email
# #     msg.set_content(body)

# #     with smtplib.SMTP(smtp_conf["server"], smtp_conf["port"]) as server:
# #         server.starttls()
# #         server.login(smtp_conf["user"], smtp_conf["pass"])
# #         server.send_message(msg)

# # @app.post("/send-email")
# # async def send_email_api(
# #     request: Request,
# #     to_email: str = Form(...),
# #     subject: str = Form(...),
# #     body: str = Form(...),
# #     provider: str = Form(...)
# # ):
# #     if provider not in SMTP_CONFIGS:
# #         return JSONResponse(content={"error": "Invalid provider"}, status_code=400)

# #     # Tăng Daily_Sent trong bộ đếm RAM
# #     daily_sent_counter[provider] = daily_sent_counter.get(provider, 0) + 1

# #     # Lấy toàn bộ input từ form
# #     form_data = await request.form()
# #     result = dict(form_data)

# #     result["to_email"] = to_email
# #     result["subject"] = subject
# #     result["body"] = body
# #     result["provider"] = provider
# #     result["assigned_account_email"] = SMTP_CONFIGS[provider]["user"]
# #     result["sent_time"] = datetime.datetime.now().isoformat()
# #     result["Daily_Sent"] = daily_sent_counter[provider]

# #     try:
# #         send_email(subject, body, to_email, SMTP_CONFIGS[provider])
# #         result["status"] = "Sent"
# #         return result
# #     except Exception as e:
# #         result["status"] = "Failed"
# #         result["error"] = str(e)
# #         return JSONResponse(content=result, status_code=500)




# # from fastapi import FastAPI, Form, Request    
# # from fastapi.responses import JSONResponse
# # import smtplib
# # from email.message import EmailMessage
# # import json
# # import datetime

# # app = FastAPI(title="Multi-SMTP Mail Sender API")

# # # Load cấu hình SMTP
# # with open("smtp_config.json", "r") as f:
# #     SMTP_CONFIGS = json.load(f)

# # # Dữ liệu đếm số lần gửi (RAM)
# # daily_sent_counter = {key: 0 for key in SMTP_CONFIGS.keys()}

# # def send_email(subject, body, to_email, smtp_conf):
# #     msg = EmailMessage()
# #     msg["Subject"] = subject
# #     msg["From"] = smtp_conf["user"]
# #     msg["To"] = to_email
# #     msg.set_content(body)

# #     with smtplib.SMTP(smtp_conf["server"], smtp_conf["port"]) as server:
# #         server.starttls()
# #         server.login(smtp_conf["user"], smtp_conf["pass"])
# #         server.send_message(msg)

# # # Tạo endpoint cho từng provider từ config
# # for provider_name, smtp_conf in SMTP_CONFIGS.items():
# #     endpoint_path = f"/send-email/{provider_name}"

# #     async def send_email_dynamic(
# #         request: Request,
# #         to_email: str = Form(...),
# #         subject: str = Form(...),
# #         body: str = Form(...),
# #         provider=provider_name  # Capture provider in closure
# #     ):
# #         # Tăng đếm gửi email
# #         daily_sent_counter[provider] = daily_sent_counter.get(provider, 0) + 1

# #         result = {
# #             "to_email": to_email,
# #             "subject": subject,
# #             "body": body,
# #             "provider": provider,
# #             "assigned_account_email": SMTP_CONFIGS[provider]["user"],
# #             "sent_time": datetime.datetime.now().isoformat(),
# #             "Daily_Sent": daily_sent_counter[provider],
# #         }

# #         try:
# #             send_email(subject, body, to_email, SMTP_CONFIGS[provider])
# #             result["status"] = "Sent"
# #             return result
# #         except Exception as e:
# #             result["status"] = "Failed"
# #             result["error"] = str(e)
# #             return JSONResponse(content=result, status_code=500)

# #     # Gắn hàm vào route động
# #     app.post(endpoint_path)(send_email_dynamic)



# from fastapi import FastAPI, Form, Request
# from fastapi.responses import JSONResponse
# import smtplib
# from email.message import EmailMessage
# import json
# import datetime

# app = FastAPI(title="Multi-SMTP Mail Sender API")

# # Load cấu hình SMTP
# with open("smtp_config.json", "r") as f:
#     SMTP_CONFIGS = json.load(f)

# def send_email(subject, body, to_email, smtp_conf):
#     msg = EmailMessage()
#     msg["Subject"] = subject
#     msg["From"] = smtp_conf["user"]
#     msg["To"] = to_email
#     msg.set_content(body)

#     with smtplib.SMTP(smtp_conf["server"], smtp_conf["port"]) as server:
#         server.starttls()
#         server.login(smtp_conf["user"], smtp_conf["pass"])
#         server.send_message(msg)

# # Tạo endpoint cho từng provider từ config
# for provider_name, smtp_conf in SMTP_CONFIGS.items():
#     endpoint_path = f"/send-email/{provider_name}"

#     async def send_email_dynamic(
#         request: Request,
#         to_email: str = Form(...),
#         subject: str = Form(...),
#         body: str = Form(...),
#         provider=provider_name  # Capture provider in closure
#     ):
#         result = {
#             "to_email": to_email,
#             "subject": subject,
#             "body": body,
#             "provider": provider,
#             "assigned_account_email": SMTP_CONFIGS[provider]["user"],
#             "sent_time": datetime.datetime.now().isoformat(),
#         }

#         try:
#             send_email(subject, body, to_email, SMTP_CONFIGS[provider])
#             result["status"] = "Sent"
#             return result
#         except Exception as e:
#             result["status"] = "Failed"
#             result["error"] = str(e)
#             return JSONResponse(content=result, status_code=500)

#     app.post(endpoint_path)(send_email_dynamic)


from fastapi import FastAPI, Form, Request, UploadFile, File
from fastapi.responses import JSONResponse
from typing import List
import smtplib
from email.message import EmailMessage
import json
import datetime
import mimetypes

app = FastAPI(title="Multi-SMTP Mail Sender API")

# Load cấu hình SMTP
with open("smtp_config.json", "r") as f:
    SMTP_CONFIGS = json.load(f)


def send_email(subject, body_html, to_email, smtp_conf, inline_images=None, attachments=None):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_conf["user"]
    msg["To"] = to_email

    # Add plain text fallback
    msg.set_content("This email contains HTML content. Please use an email client that supports HTML.")

    # Add HTML content
    msg.add_alternative(body_html, subtype="html")

    # Add inline images
    if inline_images:
        for image in inline_images:
            cid = image["cid"]
            img_data = image["data"]
            img_type = image["mime"]
            msg.get_payload()[1].add_related(
                img_data, maintype="image", subtype=img_type.split("/")[1], cid=f"<{cid}>"
            )

    # Add attachments
    if attachments:
        for file in attachments:
            filename = file["filename"]
            content = file["data"]
            mime_type, _ = mimetypes.guess_type(filename)
            maintype, subtype = mime_type.split("/") if mime_type else ("application", "octet-stream")
            msg.add_attachment(content, maintype=maintype, subtype=subtype, filename=filename)

    # Send email
    with smtplib.SMTP(smtp_conf["server"], smtp_conf["port"]) as server:
        server.starttls()
        server.login(smtp_conf["user"], smtp_conf["pass"])
        server.send_message(msg)


# Tạo endpoint cho từng provider từ config
for provider_name, smtp_conf in SMTP_CONFIGS.items():
    endpoint_path = f"/send-email/{provider_name}"

    async def send_email_dynamic(
        request: Request,
        to_email: str = Form(...),
        subject: str = Form(...),
        body: str = Form(...),
        banner: UploadFile = File(None),
        footer_img: UploadFile = File(None),
        attachments: List[UploadFile] = File([]),  # Danh sách file đính kèm
        provider=provider_name
    ):
        result = {
            "to_email": to_email,
            "subject": subject,
            "body": body,
            "provider": provider,
            "assigned_account_email": SMTP_CONFIGS[provider]["user"],
            "sent_time": datetime.datetime.now().isoformat(),
        }

        try:
            # Xử lý ảnh inline
            inline_images = []
            if banner:
                banner_data = await banner.read()
                inline_images.append({
                    "cid": "banner",
                    "data": banner_data,
                    "mime": banner.content_type
                })

            if footer_img:
                footer_data = await footer_img.read()
                inline_images.append({
                    "cid": "footer",
                    "data": footer_data,
                    "mime": footer_img.content_type
                })

            # HTML nội dung + ảnh nội tuyến
            html_body = f"""
                <html>
                <body>
                    {"<img src='cid:banner' style='width:100%;'>" if banner else ""}
                    <div>{body}</div>
                    {"<img src='cid:footer' style='width:100%; margin-top:20px;'>" if footer_img else ""}
                </body>
                </html>
            """

            # Xử lý danh sách file đính kèm
            attachment_list = []
            for file in attachments:
                content = await file.read()
                attachment_list.append({
                    "filename": file.filename,
                    "data": content
                })

            send_email(subject, html_body, to_email, SMTP_CONFIGS[provider], inline_images=inline_images, attachments=attachment_list)

            result["status"] = "Sent"
            return result

        except Exception as e:
            result["status"] = "Failed"
            result["error"] = str(e)
            return JSONResponse(content=result, status_code=500)

    app.post(endpoint_path)(send_email_dynamic)
