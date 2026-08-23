---
title: "Writing contracts"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Writing_contracts"
type: wiki
categories: Business
author: Fraser Highland Shoppe Wiki
---

IAAL. I work with technology contracts. I think that the only reason a lawyer will be scratching his head is because of the genuine unlikelihood that the customer could actually prove a fraud case against a vendor. That's not to say it's impossible, just so unlikely. What's clear is that this was not a contract case. If it was merely a contract case, it would have looked to the four corners of the agreement. The plaintiffs (the customer) had to work extra hard (i.e., $40M in legal fees hard) to prove the fraud.

Customer-clients regularly come to me with contracts that have:
#no objective criteria to measure success/failure
#all of the liability for delays, failure to perform, etc. allocated to the Customer
#do not have sufficient input from the technical people that will actually be working on the project.
#no contractual remedies for failure.
#no change management process.

Point #1 is the most important. In this case, if there were objective criteria to measure success, then the breach of contract case is simple to prove. It is like engaging in the design/plan phase of development before you even sign the contract. If a customer can't figure out what objective criteria it needs, it's probably not a good time to enter a $40M contract. Take for example, the objective criteria that the EDS software will meet the minimum process per second with 150 active users. Easy, does it do? If not, see points 2 and 4.

Point #2 is often overlooked. Customers regularly sign contracts that permit a vendor to deliver something non-conforming on the delivery date and not be in breach. The contracts are also usually written so that the additional time spent correcting the non-conforming deliverables are paid by the Customer. These are usually sneakily inserted under the "right to cure" a breach provision. At some point, the vendor (not the customer) should be paying.

Point #3 is necessary in order to establish point #1 and point #2. Management has this idea: oh we need ___ system. Let's find a vendor of ___ system. However, it is the technical people that need to set the objective criteria and then be able to test that it was met.

Point #4 is the stick with which you beat the Vendor into meeting those requirements. Every customer should be asking, "what happens if they don't deliver?" I say, "show me the money." Of course, you can customize however you see fit. Customers however don't usually ask.

Finally, point #5 is so painful its hard to write about. A lot of time and money is lost because the customer does not have a good internal change management process. In addition, the customer does not put that change management process in writing with the vendor. Any change management process should be coordinated through a project manager. The process should require 1. estimates of cost and 2. affect on time line. These should require signature of someone higher up the chain than the project manager if there is a big impact on price or time--what constitutes a "big impact" should be spelled out (e.g., more than $10,000 or more than a 1 week).

As a last tidbit: technology people need to STOP SIGNING AGREEMENTS WITHOUT A REAL LEGAL REVIEW. This includes the stupid little EULAs that you click ok to. That includes the purchase of off the shelf software. That includes signing up a third party for professional services. Those words mean things. Spending $1-3K now saves a boat load on the back end.

===Software Licenses===
Some companies will register the software purchased as an asset, and that is the procedure they must follow. They need a contract that specifies the license terms. There also has to be someone they can complain to, or contact to make improvements, or at least explain some code so they can make improvements (if you allow that). This is their procedure for operating business responsibly and that's fine.

Also as someone else mentioned, they might have to have their legal department, or paid external lawyers, analyze carefully an open source contract for viral bits. If they can write the contract for you it is easiest but make sure it contains what is shown below. Or you could use a template on the web.

People here telling you to tell them to buzz off if they won't accept BSD, etc. are not in business, and that's what is scary. Open source programmers need to be able to make a living in order to support doing their open source work, so a company asking you for a commercial license for that exact work you have already done is fabulous! Unless you have a job where you are paid to write open source software, this is ideal I should think. More like that and you wouldn't need to do other commercial work, right?

A commercial license costs money; no real company buys software for $1. The code may be exactly the same as the free version, it is okay to charge money for it.

All you need to do is make it easy for your client to purchase the a non-exclusive license to your product. This is actually an opportunity for you. You can make some money now, have a possibility for a support contract or more commercial work in the future, and you can say the code is used in a commercial product, which speaks of its quality.

Things you should specify (off the top of my head - maybe you can find some more information elsewhere):

Your (or your company's) name and address, and theirs. At the bottom, your name and the person on their side, with signatures.

Disclaimer of your liability: That the software is provided on an as-is basis and you the vendor have absolutely no liability for any defect in it, nor for any losses that may ensue through its use, or its legality in some jurisdiction, nor it is intended for illegal uses, or use in mission critical applications, etc. There is plenty of boilerplate around you can find that says this. (Assuming they are just buying something of yours and they aren't hiring you to create something for them. If they were, you'd have to guarantee against fatal-level defects, and that it meets a carefully agreed-on specification. Things like behavior in a cluster, usability on a certain architecture, 64-bit, Y2K or security related vulnerabilities would then require you to maintain it. You should add in it that any work to make improvements or repair bugs will be charged separately.)

The price. Charge them a reasonable price for it, this is a commercial license and you can include some support with it. If you include 10 hours support for free then maybe $1000 is okay, or more it depends on what the amount of code is of course. Charge for additional work you do at a certain hourly rate too if you want. Maybe you could discuss that here. You could sound them off about the price verbally. Priced beyond a certain threshold will make the decision get booted up higher.
The deliverables. Usually they need something physical. Make a CD with a nice label, write a short instruction manual, and print it out on paper (also included as a PDF or text file inside the CD). The CD and manual are physical assets that they can put in the vault and have available for software audits.

Your responsibility to support them. You may be tempted to say support is free forever, but don't do that, it costs you your time and they want value. Say limited support for a short amount of time and if they want it you can make some separate consulting or support contract with them.
If they are paying you then you can afford to provide them with support to get up and running, or to discuss with their engineers, etc. to a certain extent.

The extent of the license being granted.
- The purpose for which it is being used.
- The territory in which it can be used.
- ability to resell / re-license / redistribute / embed software in other products or not
- ability to reprint / redistribute / translate your manual, and ownership of translations.
- ability to take your name off it or not
- If being used in-house then how many cores it can run on, or is it a site license.
- If being used in a product they sell, then is it limited to a certain product, or number of units being sold.
- use of your trademark if you have one
- maybe need to protect confidentiality, or disallowing reverse engineering, but these don't sound applicable to your case.
- Usually in a contract you say the legal jurisdiction
- Be sure you are not signing full rights and ownership over to them. It is non-exclusive.

Hope this helps. As another poster mentioned check out the SQLite commercial license sample, though it is a bit short it has wording you should use.


[[Category: Business]][[Category: Contracts]][[Category: Software]][[Category: License]]