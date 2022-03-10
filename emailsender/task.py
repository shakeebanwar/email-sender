from celery import shared_task
from time import sleep
from django.core.mail import *
from celery import Celery


# app = Celery('tasks', broker='redis://localhost:6379')
app = Celery('tasks', broker='redis://redis:6379')



@app.task

def referalCompaignEmailSend(subject,femail,count,userobj):
    try:
        if int(count) == 9:
            print("this condition")
            htmlContent = '''<p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
            <br> We just wanted to remind you one last time to take advantage of Evolution's offer to get your health back on track 👌</p>'''

        elif int(count) == 3 or  int(count) == 7:
            htmlContent = ""

            
        
        for k in userobj:
            html_content = f'''
                    <!DOCTYPE html
            PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"
            style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">

        <head>
            <meta charset="UTF-8">
            <meta content="width=device-width, initial-scale=1" name="viewport">
            <meta name="x-apple-disable-message-reformatting">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta content="telephone=no" name="format-detection">
            <title>Refer A Friend 1</title>


        </head>

        <body
            style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
            <div class="es-wrapper-color" style="background-color:#F6F6F6">
                <!--[if gte mso 9]>
                        <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
                        <v:fill type="tile" color="#f6f6f6"></v:fill>
                        </v:background>
                        <![endif]-->
                <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0"
                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top">
                    <tr style="border-collapse:collapse">
                        <td valign="top" style="padding:0;Margin:0">
                            <table class="es-content" cellspacing="0" cellpadding="0" align="center"
                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                                <tr style="border-collapse:collapse">
                                    <td align="center" style="padding:0;Margin:0">
                                        <table class="es-content-body" cellspacing="0" cellpadding="0" bgcolor="#ffffff"
                                            align="center"
                                            style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px">
                                            <tr style="border-collapse:collapse">
                                                <td align="left" bgcolor="transparent"
                                                    style="padding:0;Margin:0;padding-left:20px;padding-right:20px;background-color:transparent">
                                                    <table width="100%" cellspacing="0" cellpadding="0"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr style="border-collapse:collapse">
                                                            <td valign="top" align="center"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table width="100%" cellspacing="0" cellpadding="0"
                                                                    bgcolor="transparent"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent"
                                                                    role="presentation">
                                                                    <tr style="border-collapse:collapse">
                                                                        <td align="left"
                                                                            style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px">
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                Hey {k['recieverFirstname']}</p>
                                                                                {htmlContent}
                                                                            

                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                <br></p>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                            Your friend, {k['referFirstname']} who has been attending our clinic to get their health back on track mentioned that you may also benefit from our services.<br><br></p>
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                We're doing something AWESOME to promote our Clinic where we apply drug-free treatments to help our patients achieve their health goals to improve their quality of life 👌</p><br>


                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                Since {k['referFirstname']} has sent you our way, we are excited to be able offer you a $50 discount off of your first session which includes:</p>

                                                                                <br>
                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                👍 Comprehensive Consultation & Assessment</p>
                                                                            

                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                👍 Treatment Action Plan outlining how we will help you get back to your best</p>

                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                👍 Hands On Treatment to get you relief fast!Worth $150, saving you $50!</p>
                                                                        

                                                                                <br>
                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                So, if you can relate to any of the following, this offer is for you!</p>


                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                😫 Neck and Back Pain</p>


                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                😫 Headaches</p>



                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                😫 Stress and Anxiety</p>



                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                😫 Ongoing Health Concerns</p>


                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                👌 Looking for another way of dealing with health issues</p>


                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                🚀 Want to get your health back on track once and for all!</p>


                                                                                <br>
                                                                                <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                Click the link below and follow the prompts to secure your booking and lets make it happen! 🔥</p>
                                                                        </td>
                                                                    </tr>

                                                                
                                                                    <tr style="border-collapse:collapse">
                                                                        <td align="center" style="padding:0;Margin:0"><span
                                                                                class="es-button-border-3 es-button-border"
                                                                                style="border-style:solid;border-color:#2CB543;background:#007191;border-width:0px 0px 2px 0px;display:inline-block;border-radius:30px;width:auto;border-bottom-width:0px"><a
                                                                                    href="https://pycare.co/"
                                                                                    class="es-button es-button-2"
                                                                                    target="_blank"
                                                                                    style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#FFFFFF;font-size:18px;border-style:solid;border-color:#007191;border-width:10px 20px 10px 20px;display:inline-block;background:#007191;border-radius:30px;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-weight:normal;font-style:normal;line-height:22px;width:auto;text-align:center">Book Online Now</a></span></td>
                                                                    </tr>


                                                                    








                                                                    <tr style="border-collapse:collapse">
                                                                        <td align="left"
                                                                            style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px">
                                                                            <p
                                                                                style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                                Warm regards,<br>Evolution Medical Care
                                                                                Team&nbsp;😊</p>


                                                                            
                                                                        </td>

                                                                        
                                                                    </tr>

                                                                    <tr>
                                                                        <td align="left"
                                                                        style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px">
                                                                            <h5>Terms & Conditions:</h5>
                                                                        </td>
                                                                    </tr>

                                                                    <tr>
                                                                        <td align="left"
                                                                        style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px">
                                                                        <p  style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px"> 
                                                                            1. Referred friend must attend for a Healthcare Assessment before credit will be applied to your account.
                                                                        </p>
                                                                        </td>
                                                                    </tr>




                                                                    <tr>
                                                                        <td align="left"
                                                                        style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px">
                                                                        <p  style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px"> 
                                                                            2. Credit valid for 6 months from referral and not redeemable for cash.
                                                                        </p>
                                                                        </td>
                                                                    </tr>


                                                                    <tr>
                                                                        <td align="left"
                                                                        style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px">
                                                                        <p  style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px"> 
                                                                            3. Offer valid for Pensioner/Concession card holders.
                                                                        </p>
                                                                        </td>
                                                                    </tr>





                                                                    <tr>
                                                                        <td align="left"
                                                                        style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px">
                                                                        <p  style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px"> 
                                                                            4. If paying for services via smart saver instalments, credit will be applied to future instalments.
                                                                        </p>
                                                                        </td>
                                                                    </tr>


                                                                    <tr>
                                                                        <td align="left"
                                                                        style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px">
                                                                        <p  style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px"> 
                                                                            5. Offer valid for unlimited referrals from 01/01/2022.
                                                                        </p>
                                                                        </td>
                                                                    </tr>




                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr style="border-collapse:collapse">
                                                <td align="left" bgcolor="transparent"
                                                    style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:transparent">
                                                    <table cellspacing="0" cellpadding="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr style="border-collapse:collapse">
                                                            <td align="left" style="padding:0;Margin:0;width:560px">
                                                                <table width="100%" cellspacing="0" cellpadding="0"
                                                                    bgcolor="transparent"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;background-color:transparent;border-radius:5px;background-image:url(https://wqtoe.stripocdn.email/content/guids/CABINET_28e8faadc51ce40383edabf0bf5c1489/images/footer_compressed_600.png);background-repeat:no-repeat;background-position:left top"
                                                                    background="https://wqtoe.stripocdn.email/content/guids/CABINET_28e8faadc51ce40383edabf0bf5c1489/images/footer_compressed_600.png"
                                                                    role="presentation">
                                                                    <tr style="border-collapse:collapse">
                                                                        <td style="padding:0;Margin:0">
                                                                            <table class="es-menu" width="100%" cellspacing="0"
                                                                                cellpadding="0" role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr class="links-images-top"
                                                                                    style="border-collapse:collapse">
                                                                                    <!--[if !mso]><!-- -->
                                                                                    <td align="center" valign="top"
                                                                                        width="33.33%"
                                                                                        class="es-desk-menu-hidden es-desk-hidden"
                                                                                        style="display:none;float:left;overflow:hidden;width:33.33% !important;max-height:0;line-height:0;mso-hide:all;Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0"
                                                                                        bgcolor="transparent"><a target="_blank"
                                                                                            style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px"
                                                                                            href="tel:0247096727"><img
                                                                                                src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/phone_with_sound_waves.png"
                                                                                                alt="Call Now" title="Call Now"
                                                                                                align="absmiddle" width="30"
                                                                                                height="30"
                                                                                                style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>Call
                                                                                            Now </a></td>
                                                                                    <!--<![endif]-->
                                                                                    <!--[if !mso]><!-- -->
                                                                                    <td align="center" valign="top"
                                                                                        width="33.33%"
                                                                                        class="es-desk-menu-hidden es-desk-hidden"
                                                                                        style="display:none;float:left;overflow:hidden;width:33.33% !important;max-height:0;line-height:0;mso-hide:all;Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0"
                                                                                        bgcolor="transparent"><a target="_blank"
                                                                                            style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px"
                                                                                            href="https://evolution.book.app/"><img
                                                                                                src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/clock_calendar_icon.png"
                                                                                                alt="Book Now" title="Book Now"
                                                                                                align="absmiddle" width="30"
                                                                                                height="30"
                                                                                                style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>Book
                                                                                            Now </a></td>
                                                                                    <!--<![endif]-->
                                                                                    <!--[if !mso]><!-- -->
                                                                                    <td align="center" valign="top"
                                                                                        width="33.33%"
                                                                                        class="es-desk-menu-hidden es-desk-hidden"
                                                                                        style="display:none;float:left;overflow:hidden;width:33.33% !important;max-height:0;line-height:0;mso-hide:all;Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0"
                                                                                        bgcolor="transparent"><a target="_blank"
                                                                                            style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px"
                                                                                            href="https://goo.gl/maps/L6rxReViBoTDu6dT8"><img
                                                                                                src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/car_icon.png"
                                                                                                alt="Directions"
                                                                                                title="Directions"
                                                                                                align="absmiddle" width="30"
                                                                                                height="30"
                                                                                                style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>Directions
                                                                                        </a></td>
                                                                                    <!--<![endif]-->
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                    <tr style="border-collapse:collapse">
                                                                        <td style="padding:0;Margin:0">
                                                                            <table class="es-menu" width="100%" cellspacing="0"
                                                                                cellpadding="0" role="presentation"
                                                                                style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                                                <tr class="links-images-top"
                                                                                    style="border-collapse:collapse">
                                                                                    <td align="center" valign="top"
                                                                                        width="33.33%" class="es-mobile-hidden"
                                                                                        style="Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0"
                                                                                        bgcolor="transparent"><a target="_blank"
                                                                                            style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px"
                                                                                            href="tel:0247096727"><img
                                                                                                src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/phone_with_sound_waves.png"
                                                                                                alt="(02) 4709 6727"
                                                                                                title="(02) 4709 6727"
                                                                                                width="30" align="absmiddle"
                                                                                                height="30"
                                                                                                style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>(02)
                                                                                            4709 6727 </a></td>
                                                                                    <td align="center" valign="top"
                                                                                        width="33.33%" class="es-mobile-hidden"
                                                                                        style="Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0"
                                                                                        bgcolor="transparent"><a target="_blank"
                                                                                            style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px"
                                                                                            href="https://evolution.book.app/"><img
                                                                                                src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/clock_calendar_icon.png"
                                                                                                alt="Book Now" title="Book Now"
                                                                                                width="30" align="absmiddle"
                                                                                                height="30"
                                                                                                style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>Book
                                                                                            Now </a></td>
                                                                                    <td align="center" valign="top"
                                                                                        width="33.33%" class="es-mobile-hidden"
                                                                                        style="Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0"
                                                                                        bgcolor="transparent"><a target="_blank"
                                                                                            style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px"
                                                                                            href="https://goo.gl/maps/L6rxReViBoTDu6dT8"><img
                                                                                                src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/car_icon.png"
                                                                                                alt="6/474 High Street, Penrith, NSW, 2750"
                                                                                                title="6/474 High Street, Penrith, NSW, 2750"
                                                                                                width="30" align="absmiddle"
                                                                                                height="30"
                                                                                                style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>6/474
                                                                                            High Street, Penrith, NSW, 2750 </a>
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                            <tr style="border-collapse:collapse">
                                                <td align="left"
                                                    style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px">
                                                    <table cellpadding="0" cellspacing="0" width="100%"
                                                        style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                                                        <tr style="border-collapse:collapse">
                                                            <td align="center" valign="top"
                                                                style="padding:0;Margin:0;width:560px">
                                                                <table cellpadding="0" cellspacing="0" width="100%"
                                                                    role="presentation"
                                                                    style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">


                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </div>
        </body>

        </html>
                
                        '''
            

            
            msg = EmailMultiAlternatives(subject, html_content, femail, [k['reciever']])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        # return True


    except Exception as e:
        return Response({'status':False,'message':str(e)})  