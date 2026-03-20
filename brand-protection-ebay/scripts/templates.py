#!/usr/bin/env python3
"""
Brand Protection Templates - Complaint & Legal Templates
Brand ProtectionTemplate - Complaint and legal document templates

Packagecontain:
- Brand Registry Complaint Templates
- Cease & Desist StopInfringementLetter
- Test Buy Operation guide
- MAP Violation notice
- LegalLetterTemplate

Version: 1.0.0
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class ComplaintInfo:
    """ComplaintInformation"""
    brand_name: str
    trademark_number: Optional[str] = None
    asin: str = ""
    seller_name: str = ""
    seller_id: str = ""
    violation_type: str = ""
    evidence: str = ""
    contact_email: str = ""
    company_name: str = ""


# ============================================================
# Complaint Templates
# ============================================================

def generate_brand_registry_complaint(info: ComplaintInfo) -> str:
    """Generate Brand Registry Complaint Templates"""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 BRAND REGISTRY COMPLAINT TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Platform**: Amazon Brand Registry Portal
**URL**: https://brandregistry.amazon.com/

---

## Report Details

**Brand Name**: {info.brand_name}
**Trademark Number**: {info.trademark_number or "N/A"}
**ASIN**: {info.asin}
**Infringing Seller**: {info.seller_name} ({info.seller_id})
**Violation Type**: {info.violation_type}

---

## Complaint Text (Copy & Paste)

```
I am the brand owner of {info.brand_name} (Trademark #{info.trademark_number or "[YOUR TRADEMARK NUMBER]"}).

The seller "{info.seller_name}" (Seller ID: {info.seller_id}) is selling unauthorized/counterfeit products on ASIN {info.asin}.

Evidence:
{info.evidence or "[Describe your evidence here - screenshots, test buy results, etc.]"}

This seller is NOT an authorized reseller of our products. We request immediate removal of this seller from our listing.

Contact: {info.contact_email or "[YOUR EMAIL]"}
Company: {info.company_name or "[YOUR COMPANY NAME]"}
```

---

## Steps to Submit

1. Log into Brand Registry: https://brandregistry.amazon.com/
2. Click "Report a Violation"
3. Select violation type
4. Enter ASIN and seller information
5. Paste complaint text above
6. Upload evidence (screenshots, invoices, test buy photos)
7. Submit and note case ID

---

## Evidence Checklist

☐ Screenshots of listing showing unauthorized seller
☐ Invoice/order confirmation from test buy
☐ Photos comparing authentic vs suspected counterfeit
☐ Trademark registration certificate
☐ Authorization letter (showing seller is NOT authorized)
"""


def generate_cease_desist(info: ComplaintInfo) -> str:
    """GenerateStopInfringementLetterTemplate"""
    today = datetime.now().strftime("%B %d, %Y")
    
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 CEASE AND DESIST LETTER TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Date**: {today}

---

**CEASE AND DESIST NOTICE**

To: {info.seller_name}
Seller ID: {info.seller_id}
Re: Unauthorized Sale of {info.brand_name} Products

---

Dear {info.seller_name},

This letter serves as formal notice that you are engaging in unauthorized sale of products bearing the {info.brand_name}® trademark (Registration No. {info.trademark_number or "[TRADEMARK NUMBER]"}) on Amazon.com, specifically on ASIN: {info.asin}.

**YOU ARE NOT AN AUTHORIZED RESELLER** of {info.brand_name} products. Your unauthorized sale of these products constitutes:

1. Trademark infringement under 15 U.S.C. § 1114
2. False designation of origin under 15 U.S.C. § 1125(a)
3. Violation of Amazon's Anti-Counterfeiting Policy

**DEMAND**

We hereby demand that you:

1. Immediately cease and desist all sales of {info.brand_name} products
2. Remove all {info.brand_name} product listings from your seller account
3. Provide a written confirmation of compliance within 5 business days

**CONSEQUENCES OF NON-COMPLIANCE**

Failure to comply with this demand will result in:
- Report to Amazon Brand Registry for listing removal
- Legal action seeking injunctive relief and monetary damages
- Report to law enforcement if counterfeit goods are involved

This letter is not intended to be a complete statement of the facts or law applicable to this matter, and nothing herein should be construed as a waiver of any rights or remedies.

Sincerely,

{info.company_name or "[YOUR COMPANY NAME]"}
{info.contact_email or "[YOUR EMAIL]"}

---

## Sending Instructions

1. Send via Amazon Buyer-Seller Messaging (if available)
2. Send via seller's contact email (find in storefront)
3. Keep copies of all correspondence
4. Set 5-day deadline for response
5. Escalate to legal action if no response
"""


def generate_test_buy_guide() -> str:
    """Generate Test Buy Operation guide"""
    return """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 TEST BUY PROCEDURE GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Purpose

Test Buy is the process of purchasing products from suspected counterfeit/unauthorized sellers to collect physical evidence for your complaint.

---

## Step-by-Step Process

### 1. Preparation

☐ Create a separate Amazon buyer account (not linked to seller account)
☐ Use a different shipping address if possible
☐ Prepare camera for documentation
☐ Have authentic product ready for comparison

### 2. Purchase

☐ Select the suspected seller's offer (not Buy Box)
☐ Screenshot the product page showing seller name and price
☐ Screenshot checkout page with seller info
☐ Complete purchase and save order confirmation
☐ Note Order ID: ________________

### 3. Documentation Upon Arrival

☐ Photograph unopened package (showing shipping label)
☐ Video record unboxing process
☐ Photograph product from multiple angles
☐ Compare with authentic product side-by-side:
   - Packaging differences
   - Label/printing quality
   - Product quality/finish
   - Weight comparison
   - Serial number verification
☐ Keep all packaging materials

### 4. Evidence Organization

Create folder with:
```
test_buy_evidence/
├── 01_listing_screenshots/
├── 02_order_confirmation/
├── 03_package_photos/
├── 04_unboxing_video/
├── 05_product_comparison/
└── 06_notes.txt
```

### 5. Submit Complaint

☐ Compile all evidence
☐ Write detailed complaint (use template)
☐ Submit via Brand Registry
☐ Include Order ID in complaint
☐ Upload photos/video

---

## Evidence Checklist

**Screenshots**
☐ Listing page with seller
☐ Seller storefront
☐ Order confirmation
☐ Shipping confirmation
☐ Delivery confirmation

**Photos**
☐ Package exterior (4+ angles)
☐ Shipping label close-up
☐ Product in packaging
☐ Product removed
☐ Side-by-side with authentic
☐ Close-up of differences

**Documents**
☐ Invoice from test buy
☐ Authentication certificate (if available)
☐ Trademark registration

---

## Timeline

Day 1: Place order
Day 3-7: Receive package
Day 7-8: Document and compare
Day 8-10: Compile and submit complaint
Day 10-21: Amazon review period

---

## Cost Tracking

| Item | Cost |
|------|------|
| Test Buy Product | $_____ |
| Shipping | $_____ |
| Return Shipping | $_____ |
| Total | $_____ |

*Note: May be recoverable in legal action*
"""


def generate_map_violation_notice(info: ComplaintInfo, violation_price: float, map_price: float) -> str:
    """Generate MAP Violation notice"""
    today = datetime.now().strftime("%B %d, %Y")
    discount = (map_price - violation_price) / map_price * 100
    
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 MAP VIOLATION NOTICE TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Date**: {today}

---

**MINIMUM ADVERTISED PRICE (MAP) VIOLATION NOTICE**

To: {info.seller_name}
Re: MAP Policy Violation - {info.brand_name}

---

Dear {info.seller_name},

This notice is to inform you that your current advertised price for {info.brand_name} products violates our Minimum Advertised Price (MAP) policy.

**Violation Details:**

| Product | ASIN | Your Price | MAP Price | Violation |
|---------|------|------------|-----------|-----------|
| {info.brand_name} | {info.asin} | ${violation_price:.2f} | ${map_price:.2f} | -{discount:.1f}% |

**MAP Policy Terms:**

As an authorized/unauthorized reseller of {info.brand_name} products, you are required to maintain advertised prices at or above the Minimum Advertised Price. This policy ensures:

- Fair competition among resellers
- Brand value protection
- Quality customer experience

**Required Action:**

Please adjust your advertised price to ${map_price:.2f} or higher within **48 hours** of receiving this notice.

**Consequences of Non-Compliance:**

Continued violation of our MAP policy may result in:
- Removal from authorized reseller program
- Report to Amazon for policy violation
- Supply chain restrictions

Please confirm compliance by replying to this notice.

Sincerely,
{info.company_name or "[YOUR COMPANY NAME]"}
{info.contact_email or "[YOUR EMAIL]"}
"""


# ============================================================
#  in textTemplate
# ============================================================

def generate_brand_registry_complaint_zh(info: ComplaintInfo) -> str:
    """Generate Brand Registry Complaint Templates ( in text)"""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 BRAND REGISTRY Complaint Templates
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Platform**: Amazon Brand Registry Portal
**URL**: https://brandregistry.amazon.com/

---

## ComplaintInformation

**BrandName**: {info.brand_name}
**TrademarkRegisternumber**: {info.trademark_number or "N/A"}
**ASIN**: {info.asin}
**InfringementSeller**: {info.seller_name} ({info.seller_id})
**InfringementCategoryType**: {info.violation_type}

---

## ComplaintText (CopyPaste)

```
I is  {info.brand_name} BrandOwner (TrademarkRegisternumber: {info.trademark_number or "[youTrademarknumber]"})。

Seller "{info.seller_name}" (Seller ID: {info.seller_id}) positive in  ASIN {info.asin} Selling unauthorized on/CounterfeitProduct。

Evidence:
{info.evidence or "[Describe your evidence here - Screenshot、TestPurchaseResult etc]"}

 should Sellernot is WeProductAuthorized distributor of。WeRequestImmediately will  this Seller from We Listing  in Remove。

Contact info: {info.contact_email or "[Your email]"}
CompanyName: {info.company_name or "[youCompanyname]"}
```

---

## SubmitStep

1. Login Brand Registry: https://brandregistry.amazon.com/
2. Click "Report a Violation" (ReportInfringement)
3. ChoiceInfringementCategoryType
4. Input ASIN AndSellerInformation
5. PasteAboveComplaintText
6. UploadEvidence (Screenshot、Invoice、Test Buy Photo)
7. SubmitandRecord Case ID

---

## EvidenceList

☐ Show notAuthorizedSeller Listing Screenshot
☐ Test Buy Invoice/OrderConfirm
☐ Authentic vs suspected counterfeitComparisonPhoto
☐ Trademark registration certificate
☐ Authorizedbook (Proof should SellerNot obtainedAuthorized)
"""


def generate_test_buy_guide_zh() -> str:
    """Generate Test Buy Operation guide ( in text)"""
    return """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 TEST BUY Operation guide
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## item

Test Buy (TestPurchase) Is fromSuspiciousCounterfeit/notAuthorizedSeller at PurchaseProduct，Process of collecting physical evidence for complaint。

---

## Operation process

### 1. Preparation work

☐ CreateIndependent Amazon BuyerAccount (not need  and SellerAccountAssociate)
☐ Use different deliveryAddress
☐ Prepare camera for recording
☐ Prepare authentic product forComparison

### 2. Purchase

☐ ChoiceSuspiciousSellerQuote (not need select Buy Box)
☐ ScreenshotProductPage，DisplaySellerNameAndPrice
☐ ScreenshotSettlementPage，PackagecontainSellerInformation
☐ CompletePurchaseandSaveOrderConfirm
☐ RecordOrdernumber: ________________

### 3. Receive after Record

☐ Photo of unopened package (Show shipping label)
☐ Video record unboxing process
☐  many angleDegreePhotoProduct
☐  and AuthenticSide by sideComparison:
   - PackagingDifference
   - Tag/Print quality
   - ProductQuality/Workmanship
   -  heavy quantityComparison
   - Serial number verification
☐ Keep all packaging materials

### 4. EvidenceOrganize

CreateFolder:
```
test_buy_Evidence/
├── 01_listingScreenshot/
├── 02_OrderConfirm/
├── 03_Package photo/
├── 04_UnboxingVideo/
├── 05_ProductComparison/
└── 06_Notes.txt
```

### 5. SubmitComplaint

☐ Organize all evidence
☐ Write detailed complaint (UseTemplate)
☐ Pass Brand Registry Submit
☐ Include in complaintOrdernumber
☐ Upload photo/Video

---

## Timeline

number 1 days:  below single
number 3-7 days: Receive
number 7-8 days: RecordandComparison
number 8-10 days: Organize and submit complaint
number 10-21 days: Amazon ReviewPeriod

---

## CostTrack

| Itemitem | Fee |
|------|------|
| Test Buy Product | $_____ |
| Shipping | $_____ |
| ReturnShipping | $_____ |
| Total | $_____ |

*note: Can be recovered in legal proceedings*
"""


# ============================================================
# CLI
# ============================================================

def main():
    import sys
    
    # DemoData
    info = ComplaintInfo(
        brand_name="TechGadget",
        trademark_number="US12345678",
        asin="B08XXXXXX1",
        seller_name="CheapDeals123",
        seller_id="X9Y8Z7W6V5U4T3",
        violation_type="Unauthorized Sale / Suspected Counterfeit",
        evidence="Test buy received product with different packaging and lower quality than authentic product.",
        contact_email="legal@techgadget.com",
        company_name="TechGadget Inc.",
    )
    
    lang = "zh" if "--zh" in sys.argv else "en"
    template_type = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "all"
    
    if template_type == "complaint" or template_type == "all":
        if lang == "zh":
            print(generate_brand_registry_complaint_zh(info))
        else:
            print(generate_brand_registry_complaint(info))
    
    if template_type == "cease" or template_type == "all":
        print(generate_cease_desist(info))
    
    if template_type == "testbuy" or template_type == "all":
        if lang == "zh":
            print(generate_test_buy_guide_zh())
        else:
            print(generate_test_buy_guide())
    
    if template_type == "map" or template_type == "all":
        print(generate_map_violation_notice(info, 18.99, 29.99))


if __name__ == "__main__":
    main()
