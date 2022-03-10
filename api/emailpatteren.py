from django.core.mail import EmailMultiAlternatives


###cancelation publicity
def publicity(subject,femail,toemail,host):
   
    try:
        html_content = f'''
            
        <!doctype html>
        <html lang="en-US">
        <head>
            <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
            <title>Reset Password Email Template</title>
            <meta name="description" content="Reset Password Email Template.">
            
        </head>
        <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
            <!--100% body table-->
            <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8"
                style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
                <tr>
                    <td>
                        <table style="background-color: #f2f3f8; max-width:670px;  margin:0 auto;" width="100%" border="0"
                            align="center" cellpadding="0" cellspacing="0">
                            <tr>
                                <td style="height:80px;">&nbsp;</td>
                            </tr>
                            
                            <tr>
                                <td style="height:20px;">&nbsp;</td>
                            </tr>
                            <tr>
                                <td>
                                    <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                        style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                        <tr>
                                            <td style="height:40px;">&nbsp;</td>
                                        </tr>
                                        <tr>
                                            <td style="padding:0 35px;">
                                                <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Title</h1>
                                                <span
                                                    style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span>
                                                <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">
                                               Promotion Content
                                                </p>

                                                 <a href="{host}/emailconfirmation/{toemail}"
                                                    style="background:#157;text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">Click Here
                                            </a>
                                             
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="height:40px;">&nbsp;</td>
                                        </tr>
                                    </table>
                                </td>
                            <tr>
                                <td style="height:20px;">&nbsp;</td>
                            </tr>
                            
                            <tr>
                                <td style="height:80px;">&nbsp;</td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <!--/100% body table-->
        </body>
        </html>
            '''

        msg = EmailMultiAlternatives(subject, html_content, femail, [toemail])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    
    
    except:
        return False






###when more than 3 appointment
def review(subject,femail,toemail,ratingurl):
    try:
        html_content = f'''
            
        <!doctype html>
        <html lang="en-US">
        <head>
            <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
            <title>Reset Password Email Template</title>
            <meta name="description" content="Reset Password Email Template.">
            
        </head>
        <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
            <!--100% body table-->
            <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8"
                style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
                <tr>
                    <td>
                        <table style="background-color: #f2f3f8; max-width:670px;  margin:0 auto;" width="100%" border="0"
                            align="center" cellpadding="0" cellspacing="0">
                            <tr>
                                <td style="height:80px;">&nbsp;</td>
                            </tr>
                            
                            <tr>
                                <td style="height:20px;">&nbsp;</td>
                            </tr>
                            <tr>
                                <td>
                                    <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                        style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                        <tr>
                                            <td style="height:40px;">&nbsp;</td>
                                        </tr>
                                        <tr>
                                            <td style="padding:0 35px;">
                                                <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Feedback</h1>
                                                <span
                                                    style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span>
                                                <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">
                                               Click on the Button and enter the rating
                                                </p>

                                                 <a href="{ratingurl}"
                                                    style="background:#157;text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">Click Here
                                            </a>
                                             
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="height:40px;">&nbsp;</td>
                                        </tr>
                                    </table>
                                </td>
                            <tr>
                                <td style="height:20px;">&nbsp;</td>
                            </tr>
                            
                            <tr>
                                <td style="height:80px;">&nbsp;</td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <!--/100% body table-->
        </body>
        </html>
            '''

        msg = EmailMultiAlternatives(subject, html_content, femail, [toemail])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    
    
    except:
        return False



###Review send to email

def reviewsendtoEmail(subject,femail,toemail,ratingurl,fullname,textbody):
    try:
        html_content = f'''
                            <!doctype html>
            <html lang="en-US">
            <head>
                <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
                <title>Feedback Alert</title>
                <meta name="description" content="Feedback Alert">
                
            </head>
            <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
                <!--100% body table-->
                <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8"
                    style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
                    <tr>
                        <td>
                            <table style="background-color: #f2f3f8; max-width:670px;  margin:0 auto;" width="100%" border="0"
                                align="center" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td style="height:80px;">&nbsp;</td>
                                </tr>
                                
                                <tr>
                                    <td style="height:20px;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td>
                                        <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                            style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                            <tr>
                                                <td style="height:40px;">&nbsp;</td>
                                            </tr>
                                            <tr>
                                                <td style="padding:0 35px;">
                                                    <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Feedback Alert</h1>
                                                    <span
                                                        style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span>
                                                    <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">
                                                {fullname} {textbody}
                                                    </p>

                                                    <a href="{ratingurl}"
                                                        style="background:#157;text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">Click Here
                                                </a>
                                                
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="height:40px;">&nbsp;</td>
                                            </tr>
                                        </table>
                                    </td>
                                <tr>
                                    <td style="height:20px;">&nbsp;</td>
                                </tr>
                                
                                <tr>
                                    <td style="height:80px;">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
                <!--/100% body table-->
            </body>
            </html>
            
                        '''

        msg = EmailMultiAlternatives(subject, html_content, femail, [toemail])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True

    
    except:
        return False





###when referal link is used to book appointment
def statusDoneEmail(subject,femail,toemail,fname,lname):
    try:
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
                                                                        Hi {fname} {lname}!</p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        <br></p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        We just wanted to say thank you for referring your friends/family. Thanks to you, we are looking forward to helping them get their health back on track!🙏<br><br></p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        As a way of saying 'Thank You', we are pleased to advise that we have applied a a $50 credit to your account that you can use towards your next booking!</p><br>


                                                                        <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        As always, if you know anyone else that you think would benefit from our services, please click the button below & refer your friends via Email, SMS, or Social Media.</p>
                                                                  
                                                                </td>
                                                            </tr>
                                                            <tr style="border-collapse:collapse">
                                                                <td align="center" style="padding:0;Margin:0"><span
                                                                        class="es-button-border-3 es-button-border"
                                                                        style="border-style:solid;border-color:#2CB543;background:#007191;border-width:0px 0px 2px 0px;display:inline-block;border-radius:30px;width:auto;border-bottom-width:0px"><a
                                                                            href="https://pycare.co/"
                                                                            class="es-button es-button-2"
                                                                            target="_blank"
                                                                            style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#FFFFFF;font-size:18px;border-style:solid;border-color:#007191;border-width:10px 20px 10px 20px;display:inline-block;background:#007191;border-radius:30px;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-weight:normal;font-style:normal;line-height:22px;width:auto;text-align:center">Refer
                                                                            &amp; Earn $50 NOW</a></span></td>
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

        msg = EmailMultiAlternatives(subject, html_content, femail, [toemail])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True

    
    except:
        return False






###Thankyou Email after every 4 appointment
def thankyouEmail(subject,femail,toemail):
    try:
        html_content = f'''
                            <!doctype html>
            <html lang="en-US">
            <head>
                <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
                <title>Feedback Alert</title>
                <meta name="description" content="Feedback Alert">
                
            </head>
            <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
                <!--100% body table-->
                <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8"
                    style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
                    <tr>
                        <td>
                            <table style="background-color: #f2f3f8; max-width:670px;  margin:0 auto;" width="100%" border="0"
                                align="center" cellpadding="0" cellspacing="0">
                                <tr>
                                    <td style="height:80px;">&nbsp;</td>
                                </tr>
                                
                                <tr>
                                    <td style="height:20px;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td>
                                        <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                            style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                            <tr>
                                                <td style="height:40px;">&nbsp;</td>
                                            </tr>
                                            <tr>
                                                <td style="padding:0 35px;">
                                                    <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Evolution Medical Care</h1>
                                                    <span
                                                        style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span>
                                                    <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">
                                                            Thankyou very much
                                                    </p>

                                                 
                                                
                                                </td>
                                            </tr>
                                            <tr>
                                                <td style="height:40px;">&nbsp;</td>
                                            </tr>
                                        </table>
                                    </td>
                                <tr>
                                    <td style="height:20px;">&nbsp;</td>
                                </tr>
                                
                                <tr>
                                    <td style="height:80px;">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
                <!--/100% body table-->
            </body>
            </html>
            
                        '''

        msg = EmailMultiAlternatives(subject, html_content, femail, [toemail])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True

    
    except:
        return False




##Referal compaign
def referalCompaign(subject,firstname,femail,toemail,host):
  
    try:
        html_content = f'''
            
        <!doctype html>
        <html lang="en-US">
        <head>
            <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
            <title>Reset Password Email Template</title>
            <meta name="description" content="Reset Password Email Template.">
            
        </head>
        <body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
            <!--100% body table-->
            <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8"
                style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
                <tr>
                    <td>
                        <table style="background-color: #f2f3f8; max-width:670px;  margin:0 auto;" width="100%" border="0"
                            align="center" cellpadding="0" cellspacing="0">
                            <tr>
                                <td style="height:80px;">&nbsp;</td>
                            </tr>
                            
                            <tr>
                                <td style="height:20px;">&nbsp;</td>
                            </tr>
                            <tr>
                                <td>
                                    <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                        style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                        <tr>
                                            <td style="height:40px;">&nbsp;</td>
                                        </tr>
                                        <tr>
                                            <td style="padding:0 35px;">
                                                <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Referral Campaign</h1>
                                                <br>
                                                <p style="color:#455056; font-size:15px;line-height:24px; margin:0;text-align: start;">
New Referral Program at Evolution Medical Care! <br>
Hi {firstname}, Evolution Medical Care is excited to have you in our new Friends & Family Referral Program! 
How it works Click the button below & share the offer with your friends via Email, Text Message, or Social Media. <br><br>
Each share is automatically tracked back to you. You could share with ten or ten thousand friends and we will know the referral came from you.<br><br>For each of your friends, who take advantage of our offer and signs up and attends for a Healthcare Assessment, you and your friend will earn a $50 credit you can each use towards the next service! <br>Refer & Earn $50 NOW</p>
<div style="width="100% text-align="center">
<a href="{host}"style="background:#157;text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">Click Here
                                                </a>

                                              
                                             
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="height:40px;">&nbsp;</td>
                                        </tr>
                                    </table>
                                </td>
                            <tr>
                                <td style="height:20px;">&nbsp;</td>
                            </tr>
                            
                            <tr>
                                <td style="height:80px;">&nbsp;</td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <!--/100% body table-->
        </body>
        </html>
            '''

        msg = EmailMultiAlternatives(subject, html_content, femail, [toemail])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    
    
    except:
        return False



###Screenshot detail

def screenshot(subject,femail,toemail,data):
  
    try:

        html_content = ""
        for j in data:
        
            morninglist = ""
            afternoon = ""
            for k in j['morning']:
               
                morninglist = morninglist + f"""<button style="width: 100%; background-color: #007191; color: white; border-radius: 4px; outline: none; border: none; padding: 8px; margin: 5px; cursor: pointer;">{k}</button>"""
            

            for l in j['afternoon']:
              
                afternoon = afternoon + f"""<button style="width: 100%; background-color: #007191; color: white; border-radius: 4px; outline: none; border: none; padding: 8px; margin: 5px; cursor: pointer;">{l}</button>"""


            
            html_content = html_content + f'''

            <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body>
        <!-- 1st -->

        <div style="width: 100%; ">
            <div style="width: 600px; margin: auto; border-radius: 5px; box-shadow: inset 0 4px 0 0 #007191; margin-block: 20px; ">
                <table style="width: 100%; margin: auto;" cellpadding="12"
                    cellspacing="0">
                    <tbody>
                        <tr>
                            <td><h3 style="color: grey; margin-bottom: 0%;">{j['day']}</h3></td>
                        </tr>
                        <tr>
                            <td style="width: 50%; text-align: center;">
                                <h4 style="color: grey; margin: 0%;">Morning</h4>
                                <!-- <button style="width: 100%; background-color: #007191; color: white; border-radius: 4px; outline: none; border: none; padding: 8px; margin: 5px;">7:00am</button> -->
                            </td>
                            <td style="width: 50%; text-align: center;">
                                <h4 style="color: grey; margin: 0%;">Afternoon</h4>
                                <!-- <button style="width: 100%; background-color: #007191; color: white; border-radius: 4px; outline: none; border: none; padding: 8px; margin: 5px;">12:00pm</button> -->
                            </td>
                        </tr>
                        <tr>
                            <td style="width: 50%; text-align: center; padding-top: 0%; vertical-align:top;">
                                <!-- <h4 style="color: grey; margin: 0%;">Morning</h4> -->
                                    
                                    {morninglist}
                            </td>
                            <td style="width: 50%; text-align: center; padding-top: 0%; vertical-align:top;">
                                {afternoon}
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>




    </body>

    </html>
            
            '''

        emailList = ["jawadsheikh224@gmail.com","test@evolutionmc.com.au","test1@evolutionmc.com.au","test2@evolutionmc.com.au","test3@evolutionmc.com.au","Shabih_haider1@outlook.com","shakeebanwar250@gmail.com","shoaibbilal101@gmail.com","mf4639@gmail.com"]
        
        msg = EmailMultiAlternatives(subject, html_content, femail, emailList)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
        
    
    except:
        return False





##Referal compaign Cronjob

def referalCronjobTemplate(subject,femail,toemail,templateContent):
    try:
        html_content = f'''
                            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
                <head>
                <meta charset="UTF-8">
                <meta content="width=device-width, initial-scale=1" name="viewport">
                <meta name="x-apple-disable-message-reformatting">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta content="telephone=no" name="format-detection">
                <title>Refer A Friend 1</title>


                </head>
                <body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0">
                <div class="es-wrapper-color" style="background-color:#F6F6F6">
                <!--[if gte mso 9]>
                <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
                <v:fill type="tile" color="#f6f6f6"></v:fill>
                </v:background>
                <![endif]-->
                <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top">
                <tr style="border-collapse:collapse">
                <td valign="top" style="padding:0;Margin:0">
                <table class="es-content" cellspacing="0" cellpadding="0" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%">
                <tr style="border-collapse:collapse">
                <td align="center" style="padding:0;Margin:0">
                <table class="es-content-body" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#FFFFFF;width:600px">
                <tr style="border-collapse:collapse">
                <td align="left" bgcolor="transparent" style="padding:0;Margin:0;padding-left:20px;padding-right:20px;background-color:transparent">
                <table width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                <tr style="border-collapse:collapse">
                <td valign="top" align="center" style="padding:0;Margin:0;width:560px">
                <table width="100%" cellspacing="0" cellpadding="0" bgcolor="transparent" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent" role="presentation">
               

                {templateContent}


             
                <tr style="border-collapse:collapse">
                <td align="left" style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:30px;padding-right:30px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">Warm regards,<br>Evolution Medical Care Team&nbsp;😊</p></td>


                   <tr style="border-collapse:collapse">
                <td align="center" style="padding:0;Margin:0"><span class="es-button-border-3 es-button-border" style="border-style:solid;border-color:#2CB543;background:#007191;border-width:0px 0px 2px 0px;display:inline-block;border-radius:30px;width:auto;border-bottom-width:0px"><a href="https://pycare.co/" class="es-button es-button-2" target="_blank" style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#FFFFFF;font-size:18px;border-style:solid;border-color:#007191;border-width:10px 20px 10px 20px;display:inline-block;background:#007191;border-radius:30px;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-weight:normal;font-style:normal;line-height:22px;width:auto;text-align:center">Refer &amp; Earn $50 NOW</a></span></td>
                </tr>
                </tr>
                </table></td>
                </tr>
                </table></td>
                </tr>
                <tr style="border-collapse:collapse">
                <td align="left" bgcolor="transparent" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px;background-color:transparent">
                <table cellspacing="0" cellpadding="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                <tr style="border-collapse:collapse">
                <td align="left" style="padding:0;Margin:0;width:560px">
                <table width="100%" cellspacing="0" cellpadding="0" bgcolor="transparent" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;background-color:transparent;border-radius:5px;background-image:url(https://wqtoe.stripocdn.email/content/guids/CABINET_28e8faadc51ce40383edabf0bf5c1489/images/footer_compressed_600.png);background-repeat:no-repeat;background-position:left top" background="https://wqtoe.stripocdn.email/content/guids/CABINET_28e8faadc51ce40383edabf0bf5c1489/images/footer_compressed_600.png" role="presentation">
                <tr style="border-collapse:collapse">
                <td style="padding:0;Margin:0">
                <table class="es-menu" width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                <tr class="links-images-top" style="border-collapse:collapse">
                <!--[if !mso]><!-- -->
                <td align="center" valign="top" width="33.33%" class="es-desk-menu-hidden es-desk-hidden" style="display:none;float:left;overflow:hidden;width:33.33% !important;max-height:0;line-height:0;mso-hide:all;Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0" bgcolor="transparent"><a target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px" href="tel:0247096727"><img src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/phone_with_sound_waves.png" alt="Call Now" title="Call Now" align="absmiddle" width="30" height="30" style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>Call Now </a></td>
                <!--<![endif]-->
                <!--[if !mso]><!-- -->
                <td align="center" valign="top" width="33.33%" class="es-desk-menu-hidden es-desk-hidden" style="display:none;float:left;overflow:hidden;width:33.33% !important;max-height:0;line-height:0;mso-hide:all;Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0" bgcolor="transparent"><a target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px" href="https://evolution.book.app/"><img src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/clock_calendar_icon.png" alt="Book Now" title="Book Now" align="absmiddle" width="30" height="30" style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>Book Now </a></td>
                <!--<![endif]-->
                <!--[if !mso]><!-- -->
                <td align="center" valign="top" width="33.33%" class="es-desk-menu-hidden es-desk-hidden" style="display:none;float:left;overflow:hidden;width:33.33% !important;max-height:0;line-height:0;mso-hide:all;Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0" bgcolor="transparent"><a target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px" href="https://goo.gl/maps/L6rxReViBoTDu6dT8"><img src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/car_icon.png" alt="Directions" title="Directions" align="absmiddle" width="30" height="30" style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>Directions </a></td>
                <!--<![endif]-->
                </tr>
                </table></td>
                </tr>
                <tr style="border-collapse:collapse">
                <td style="padding:0;Margin:0">
                <table class="es-menu" width="100%" cellspacing="0" cellpadding="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                <tr class="links-images-top" style="border-collapse:collapse">
                <td align="center" valign="top" width="33.33%" class="es-mobile-hidden" style="Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0" bgcolor="transparent"><a target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px" href="tel:0247096727"><img src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/phone_with_sound_waves.png" alt="(02) 4709 6727" title="(02) 4709 6727" width="30" align="absmiddle" height="30" style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>(02) 4709 6727 </a></td>
                <td align="center" valign="top" width="33.33%" class="es-mobile-hidden" style="Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0" bgcolor="transparent"><a target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px" href="https://evolution.book.app/"><img src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/clock_calendar_icon.png" alt="Book Now" title="Book Now" width="30" align="absmiddle" height="30" style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>Book Now </a></td>
                <td align="center" valign="top" width="33.33%" class="es-mobile-hidden" style="Margin:0;padding-left:5px;padding-right:5px;padding-top:25px;padding-bottom:15px;border:0" bgcolor="transparent"><a target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#ffffff;font-size:14px" href="https://goo.gl/maps/L6rxReViBoTDu6dT8"><img src="https://wqtoe.stripocdn.email/content/guids/CABINET_0719e868f19b059f1129de97f07e6d72/images/car_icon.png" alt="6/474 High Street, Penrith, NSW, 2750" title="6/474 High Street, Penrith, NSW, 2750" width="30" align="absmiddle" height="30" style="display:inline-block !important;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;padding-bottom:5px"><br>6/474 High Street, Penrith, NSW, 2750 </a></td>
                </tr>
                </table></td>
                </tr>
                </table></td>
                </tr>
                </table></td>
                </tr>
                <tr style="border-collapse:collapse">
                <td align="left" style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px">
                <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">
                <tr style="border-collapse:collapse">
                <td align="center" valign="top" style="padding:0;Margin:0;width:560px">
                <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px">


                </table></td>
                </tr>
                </table></td>
                </tr>
                </table></td>
                </tr>
                </table></td>
                </tr>
                </table>
                </div>
                </body>
                </html>
                            
        
                '''

        msg = EmailMultiAlternatives(subject, html_content, femail, toemail)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True


    except:
        return False




###When new user register

def registrationEmail(subject,fname,lname,femail,toemail):

    try:
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
                                                                        Hi {fname} {lname}!</p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        <br></p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        We just wanted to say thank you for registering
                                                                        for our Friends and Family Referral System. 🙏
                                                                        We're looking forward to helping out your
                                                                        network of friends and family 👌 &amp; Family
                                                                        Referral Program!<br><br></p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        <b>How our Referral System works? </b>If you
                                                                        think that one of your friends or family would
                                                                        also benefit from our services, click the button
                                                                        below and register your details to refer them so
                                                                        that we can know that it's from you!</p><br>


                                                                        <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        For each of your friends who take advantage of
                                                                        our offer and attends for a Healthcare
                                                                        Assessment, you and your friend will earn a $50
                                                                        credit you can each use towards your next
                                                                        booking!</p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        <br>Click the button below & refer your friends via Email, SMS, or Social Media.</p>
                                                                    
                                                                </td>
                                                            </tr>
                                                            <tr style="border-collapse:collapse">
                                                                <td align="center" style="padding:0;Margin:0"><span
                                                                        class="es-button-border-3 es-button-border"
                                                                        style="border-style:solid;border-color:#2CB543;background:#007191;border-width:0px 0px 2px 0px;display:inline-block;border-radius:30px;width:auto;border-bottom-width:0px"><a
                                                                            href="https://pycare.co/"
                                                                            class="es-button es-button-2"
                                                                            target="_blank"
                                                                            style="mso-style-priority:100 !important;text-decoration:none;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;color:#FFFFFF;font-size:18px;border-style:solid;border-color:#007191;border-width:10px 20px 10px 20px;display:inline-block;background:#007191;border-radius:30px;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-weight:normal;font-style:normal;line-height:22px;width:auto;text-align:center">Refer
                                                                            &amp; Earn $50 NOW</a></span></td>
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

        msg = EmailMultiAlternatives(subject, html_content, femail, [toemail])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True


    except:
        return False





def referalCompaignEmailSend(subject,femail,toemail,count,referalname,clientname):
    
    if int(count) == 9:
        print("this condition")
        htmlContent = '''<p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
        <br> We just wanted to remind you one last time to take advantage of Evolution's offer to get your health back on track 👌</p>'''

    elif int(count) == 3 or  int(count) == 7:
        htmlContent = ""

        
    
    
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
                                                                        Hey {clientname}</p>
                                                                        {htmlContent}
                                                                    

                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        <br></p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                       Your friend, {referalname} who has been attending our clinic to get their health back on track mentioned that you may also benefit from our services.<br><br></p>
                                                                    <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        We're doing something AWESOME to promote our Clinic where we apply drug-free treatments to help our patients achieve their health goals to improve their quality of life 👌</p><br>


                                                                        <p
                                                                        style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px">
                                                                        Since {referalname} has sent you our way, we are excited to be able offer you a $50 discount off of your first session which includes:</p>

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
    

    
    msg = EmailMultiAlternatives(subject, html_content, femail, [toemail])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return True


