# # # from fastapi import FastAPI, Form, Request
# # # from fastapi.responses import JSONResponse
# # # import smtplib
# # # from email.message import EmailMessage
# # # import json
# # # import datetime

# # # app = FastAPI(title="Multi-SMTP Mail Sender API")

# # # # Load cấu hình SMTP
# # # with open("smtp_config.json", "r") as f:
# # #     SMTP_CONFIGS = json.load(f)

# # # # Dữ liệu đếm số lần gửi (lưu tạm trong RAM)
# # # daily_sent_counter = {key: 0 for key in SMTP_CONFIGS.keys()}

# # # def send_email(subject, body, to_email, smtp_conf):
# # #     msg = EmailMessage()
# # #     msg["Subject"] = subject
# # #     msg["From"] = smtp_conf["user"]
# # #     msg["To"] = to_email
# # #     msg.set_content(body)

# # #     with smtplib.SMTP(smtp_conf["server"], smtp_conf["port"]) as server:
# # #         server.starttls()
# # #         server.login(smtp_conf["user"], smtp_conf["pass"])
# # #         server.send_message(msg)

# # # @app.post("/send-email")
# # # async def send_email_api(
# # #     request: Request,
# # #     to_email: str = Form(...),
# # #     subject: str = Form(...),
# # #     body: str = Form(...),
# # #     provider: str = Form(...)
# # # ):
# # #     if provider not in SMTP_CONFIGS:
# # #         return JSONResponse(content={"error": "Invalid provider"}, status_code=400)

# # #     # Tăng Daily_Sent trong bộ đếm RAM
# # #     daily_sent_counter[provider] = daily_sent_counter.get(provider, 0) + 1

# # #     # Lấy toàn bộ input từ form
# # #     form_data = await request.form()
# # #     result = dict(form_data)

# # #     result["to_email"] = to_email
# # #     result["subject"] = subject
# # #     result["body"] = body
# # #     result["provider"] = provider
# # #     result["assigned_account_email"] = SMTP_CONFIGS[provider]["user"]
# # #     result["sent_time"] = datetime.datetime.now().isoformat()
# # #     result["Daily_Sent"] = daily_sent_counter[provider]

# # #     try:
# # #         send_email(subject, body, to_email, SMTP_CONFIGS[provider])
# # #         result["status"] = "Sent"
# # #         return result
# # #     except Exception as e:
# # #         result["status"] = "Failed"
# # #         result["error"] = str(e)
# # #         return JSONResponse(content=result, status_code=500)




# # # from fastapi import FastAPI, Form, Request    
# # # from fastapi.responses import JSONResponse
# # # import smtplib
# # # from email.message import EmailMessage
# # # import json
# # # import datetime

# # # app = FastAPI(title="Multi-SMTP Mail Sender API")

# # # # Load cấu hình SMTP
# # # with open("smtp_config.json", "r") as f:
# # #     SMTP_CONFIGS = json.load(f)

# # # # Dữ liệu đếm số lần gửi (RAM)
# # # daily_sent_counter = {key: 0 for key in SMTP_CONFIGS.keys()}

# # # def send_email(subject, body, to_email, smtp_conf):
# # #     msg = EmailMessage()
# # #     msg["Subject"] = subject
# # #     msg["From"] = smtp_conf["user"]
# # #     msg["To"] = to_email
# # #     msg.set_content(body)

# # #     with smtplib.SMTP(smtp_conf["server"], smtp_conf["port"]) as server:
# # #         server.starttls()
# # #         server.login(smtp_conf["user"], smtp_conf["pass"])
# # #         server.send_message(msg)

# # # # Tạo endpoint cho từng provider từ config
# # # for provider_name, smtp_conf in SMTP_CONFIGS.items():
# # #     endpoint_path = f"/send-email/{provider_name}"

# # #     async def send_email_dynamic(
# # #         request: Request,
# # #         to_email: str = Form(...),
# # #         subject: str = Form(...),
# # #         body: str = Form(...),
# # #         provider=provider_name  # Capture provider in closure
# # #     ):
# # #         # Tăng đếm gửi email
# # #         daily_sent_counter[provider] = daily_sent_counter.get(provider, 0) + 1

# # #         result = {
# # #             "to_email": to_email,
# # #             "subject": subject,
# # #             "body": body,
# # #             "provider": provider,
# # #             "assigned_account_email": SMTP_CONFIGS[provider]["user"],
# # #             "sent_time": datetime.datetime.now().isoformat(),
# # #             "Daily_Sent": daily_sent_counter[provider],
# # #         }

# # #         try:
# # #             send_email(subject, body, to_email, SMTP_CONFIGS[provider])
# # #             result["status"] = "Sent"
# # #             return result
# # #         except Exception as e:
# # #             result["status"] = "Failed"
# # #             result["error"] = str(e)
# # #             return JSONResponse(content=result, status_code=500)

# # #     # Gắn hàm vào route động
# # #     app.post(endpoint_path)(send_email_dynamic)



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
# #         result = {
# #             "to_email": to_email,
# #             "subject": subject,
# #             "body": body,
# #             "provider": provider,
# #             "assigned_account_email": SMTP_CONFIGS[provider]["user"],
# #             "sent_time": datetime.datetime.now().isoformat(),
# #         }

# #         try:
# #             send_email(subject, body, to_email, SMTP_CONFIGS[provider])
# #             result["status"] = "Sent"
# #             return result
# #         except Exception as e:
# #             result["status"] = "Failed"
# #             result["error"] = str(e)
# #             return JSONResponse(content=result, status_code=500)

# #     app.post(endpoint_path)(send_email_dynamic)


# from fastapi import FastAPI, Form, Request, UploadFile, File
# from fastapi.responses import JSONResponse
# from typing import List
# import smtplib
# from email.message import EmailMessage
# import json
# import datetime
# import mimetypes

# app = FastAPI(title="Multi-SMTP Mail Sender API")

# # Load cấu hình SMTP
# with open("smtp_config.json", "r") as f:
#     SMTP_CONFIGS = json.load(f)


# def send_email(subject, body_html, to_email, smtp_conf, inline_images=None, attachments=None):
#     msg = EmailMessage()
#     msg["Subject"] = subject
#     msg["From"] = smtp_conf["user"]
#     msg["To"] = to_email

#     # Add plain text fallback
#     msg.set_content("This email contains HTML content. Please use an email client that supports HTML.")

#     # Add HTML content
#     msg.add_alternative(body_html, subtype="html")

#     # Add inline images
#     if inline_images:
#         for image in inline_images:
#             cid = image["cid"]
#             img_data = image["data"]
#             img_type = image["mime"]
#             msg.get_payload()[1].add_related(
#                 img_data, maintype="image", subtype=img_type.split("/")[1], cid=f"<{cid}>"
#             )

#     # Add attachments
#     if attachments:
#         for file in attachments:
#             filename = file["filename"]
#             content = file["data"]
#             mime_type, _ = mimetypes.guess_type(filename)
#             maintype, subtype = mime_type.split("/") if mime_type else ("application", "octet-stream")
#             msg.add_attachment(content, maintype=maintype, subtype=subtype, filename=filename)

#     # Send email
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
#         banner: UploadFile = File(None),
#         footer_img: UploadFile = File(None),
#         attachments: List[UploadFile] = File([]),  # Danh sách file đính kèm
#         provider=provider_name
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
#             # Xử lý ảnh inline
#             inline_images = []
#             if banner:
#                 banner_data = await banner.read()
#                 inline_images.append({
#                     "cid": "banner",
#                     "data": banner_data,
#                     "mime": banner.content_type
#                 })

#             if footer_img:
#                 footer_data = await footer_img.read()
#                 inline_images.append({
#                     "cid": "footer",
#                     "data": footer_data,
#                     "mime": footer_img.content_type
#                 })

#             # HTML nội dung + ảnh nội tuyến
#             html_body = f"""
#             <html>
#             <body style="font-family: Arial, sans-serif; line-height: 1.6;">
#                 <div style="margin-bottom: 20px;">
#                 {body}  <!-- Nội dung chính đã format -->
#                 </div>
                
#                 {"<div style='margin-top: 30px;'><img src='cid:banner' style='width:100%;'></div>" if banner else ""}

#                 {"<div style='margin-top: 30px; text-align: center;'><img src='cid:footer' style='width:200px;'></div>" if footer_img else ""}
                
#                 <p style="margin-top: 40px; font-size: 14px; color: gray;">
#                 Tài liệu đính kèm phía dưới email này.
#                 </p>
#             </body>
#             </html>
#             """
#             # Xử lý danh sách file đính kèm
#             attachment_list = []
#             for file in attachments:
#                 content = await file.read()
#                 attachment_list.append({
#                     "filename": file.filename,
#                     "data": content
#                 })

#             send_email(subject, html_body, to_email, SMTP_CONFIGS[provider], inline_images=inline_images, attachments=attachment_list)

#             result["status"] = "Sent"
#             return result

#         except Exception as e:
#             result["status"] = "Failed"
#             result["error"] = str(e)
#             return JSONResponse(content=result, status_code=500)

#     app.post(endpoint_path)(send_email_dynamic)


from fastapi import FastAPI, Form, Request
from fastapi.responses import JSONResponse
import smtplib
from email.message import EmailMessage
import json
import datetime
import mimetypes
import aiohttp

app = FastAPI(title="Email API: 1 PDF attach + 2 inline images from Drive")

# Load cấu hình SMTP
with open("smtp_config.json", "r") as f:
    SMTP_CONFIGS = json.load(f)

# Tải file từ Google Drive
async def download_drive_file(file_id, filename_hint=None):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            content_type = response.headers.get("Content-Type", "application/octet-stream")
            return {
                "filename": filename_hint or f"{file_id}.bin",
                "data": content,
                "mime": content_type
            }

# Gửi email
def send_email(subject, body_html, to_email, smtp_conf, inline_images=None, attachments=None):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_conf["user"]
    msg["To"] = to_email

    msg.set_content("This email contains HTML content.")
    msg.add_alternative(body_html, subtype="html")

    # Ảnh nội tuyến
    if inline_images:
        for image in inline_images:
            cid = image["cid"]
            img_data = image["data"]
            img_type = image["mime"]
            msg.get_payload()[1].add_related(
                img_data, maintype="image", subtype=img_type.split("/")[1], cid=f"<{cid}>"
            )

    # File đính kèm
    if attachments:
        for file in attachments:
            filename = file["filename"]
            content = file["data"]
            mime_type, _ = mimetypes.guess_type(filename)
            maintype, subtype = mime_type.split("/") if mime_type else ("application", "octet-stream")
            msg.add_attachment(content, maintype=maintype, subtype=subtype, filename=filename)

    with smtplib.SMTP(smtp_conf["server"], smtp_conf["port"]) as server:
        server.starttls()
        server.login(smtp_conf["user"], smtp_conf["pass"])
        server.send_message(msg)

# Tạo endpoint
for provider_name, smtp_conf in SMTP_CONFIGS.items():
    endpoint_path = f"/send-email/{provider_name}"

    async def send_email_dynamic(
        request: Request,
        to_email: str = Form(...),
        subject: str = Form(...),
        body: str = Form(...),
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
            # === Tải ảnh từ Drive để chèn vào email ===
            image1 = await download_drive_file("1rW4oTpiLxgu9Tng1LAqMAFD0FwL4-Rmw", "Pricing_Plan.jpg")
            image2 = await download_drive_file("1R7yjiry5jZi23kHmn5oe0oOH5UspqEQP", "HowToUse.jpg")

            inline_images = [
                {"cid": "image1", "data": image1["data"], "mime": image1["mime"]},
                {"cid": "image2", "data": image2["data"], "mime": image2["mime"]},
            ]

            # HTML nội dung thư
            # html_body = f"""
            # <html>
            # <body style="font-family: Arial, sans-serif;">
            #     <div>{body}</div>

            #     <div style="margin-top: 20px;">
            #         <img src="cid:image1" style="width:70%; margin-bottom: 10px;">
            #         <img src="cid:image2" style="width:40%;">
            #     </div>

            #     <p style="margin-top: 40px; font-size: 14px; color: gray;">
            #         Tài liệu PDF được đính kèm ở cuối email.
            #     </p>
            # </body>
            # </html>
            # """


            # html_body = f"""
            # <html>
            # <body style="font-family: Arial, sans-serif;">
            #     <div>{body}</div>

            #     <div style="margin-top: 20px;">
            #         <img src="cid:image1" style="width:70%; margin-bottom: 20px;">
            #     </div>

            #     <div style="display: flex; align-items: center; gap: 20px; margin-top: 10px;">
            #         <img src="cid:image2" style="width: 60%; max-width: 200px;">

            #         <div style="font-size: 14px; line-height: 1.6;">
            #             <strong>start@strongbody.ai</strong> | <a href="https://strongbody.ai" target="_blank">https://strongbody.ai</a><br>
            #             105 CECIL STREET #18 - 20 THE OCTAGON<br>
            #             SINGAPORE 069534
            #         </div>
            #     </div>

            #     <p style="margin-top: 40px; font-size: 14px; color: gray;">
            #         Tài liệu PDF được đính kèm ở cuối email.
            #     </p>
            # </body>
            # </html>
            # """
            
            # Chuyển \n trong nội dung body thành <br> để HTML hiển thị đúng dòng
            body_html = body.replace("\\n", "<br>") 

            html_body = f"""
            <html>
            <body style="font-family: Arial, sans-serif;">

                <!-- Phần nội dung ban đầu (giữ nguyên căn trái) -->
                <div>{body_html}</div>

                <!-- Từ ảnh 1 trở xuống: căn giữa từng phần -->
                <div style="text-align: center; margin-top: 20px;">
                    <!-- Ảnh 1 căn giữa -->
                    <img src="cid:image1" style="width:70%; margin-bottom: 20px; display: block; margin-left: auto; margin-right: auto;">

                    <!-- Ảnh 2 và chữ nằm ngang và căn giữa toàn khối -->
                    <div style="display: inline-flex; align-items: flex-start; gap: 20px; margin-top: 10px;">
                        <img src="cid:image2" style="width: 60%; max-width: 200px;">

                        <div style="font-size: 14px; line-height: 1.6; text-align: left;">
                            <!-- Dòng trống để đẩy nội dung xuống dòng thứ 2 -->
                            <div style="height: 1.5em;"></div>

                            <strong>start@strongbody.ai</strong> | <a href="https://strongbody.ai" target="_blank">https://strongbody.ai</a><br>
                            105 CECIL STREET #18 - 20 THE OCTAGON<br>
                            SINGAPORE 069534
                        </div>
                    </div>

                    <!-- Ghi chú -->
                    <p style="margin-top: 40px; font-size: 14px; color: gray;">
                        Tài liệu PDF được đính kèm ở cuối email.
                    </p>
                </div>

            </body>
            </html>
            """



            # === Tải file PDF từ Drive để đính kèm ===
            pdf_file = await download_drive_file("1m4bw2Wcv3kn6B4OB2eGRJ1ImVYKh8GYc", "Strongbody_Intro.pdf")
            attachments = [{
                "filename": pdf_file["filename"],
                "data": pdf_file["data"]
            }]

            # Gửi
            send_email(
                subject,
                html_body,
                to_email,
                SMTP_CONFIGS[provider],
                inline_images=inline_images,
                attachments=attachments
            )

            result["status"] = "Sent"
            return result

        except Exception as e:
            result["status"] = "Failed"
            result["error"] = str(e)
            return JSONResponse(content=result, status_code=500)

    app.post(endpoint_path)(send_email_dynamic)
