---
title: "Email Deliverability Checklist"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Email_Deliverability_Checklist"
type: wiki
categories: FHS, Marketing
author: Fraser Highland Shoppe Wiki
---

==Email Deliverability Checklist==
 http://www.digitalmarketer.com/maropost-email-deliverability/
*IP
**Shared is OK if under 50,000 emails a month
*Mandatory Authentications
**DMARC
**SPF
**DKIM
**TLS
*Positive (or Negative) Actions (big webmail providers track sender vs interaction)
**Read
**Clicked
**Replied to
**Moved to another non spam/trash folder
**sender or domain added to address book
**forwarded 
**scrolled through
**marked NOT SPAM.
*Negative Actions
**Email not read
**deleted
**not clicked
*Email Feedback Loop
**[https://support.google.com/mail/answer/6254652?hl=en Google]
**[https://www.emailfeedbackloops.com/how-to-apply-for-hotmail-feedback-loop.php Hotmail]
**Each provider has its own way of sending the feedback loop
*Email Acquisition 
**Pristine Spam traps
**Use double opt-in
**Quarantine new email addresses until confirm no hard bounce
**basic validation
***sales@
***garbage addresses such as alskalsk@test.com
*Email List Cleansing
**Recycled spam trap
**Remove inactive subscribers
*Set expectations with WELCOME email
*INCLUDE A LINK TO UNSUBSCRIBE
*INCLUDE A LINK TO THE PREFERENCE CENTER
*CONFIRM YOUR HTML
**Make sure the frontend renders correctly and the backend is bug-free!
*Plain text + html
**Not all recipients and platforms have enabled HTML – so you’ll need a plaintext and web version of the email
*Email Content
**balance text and image
**check links
**avoid base64

[[Category: Digital Marketer]]
[[Category: Email]]
[[Category: All Pages]]
[[Category: Marketing]]
[[Category: FHS]]