#!/usr/bin/env python3
"""Extra table rows so every system demo shows a full, believable dataset.

Keyed by demo file name; each value is a list of row tuples matching that
demo's `cols` definition.
"""

EXTRA_ROWS = {
    "system-crm.html": [
        ("School website", "Groupe Scolaire Kicukiro", "3.6M", "Discovery"),
        ("Fleet tracking", "Rwanda Express Logistics", "5.4M", "Proposal"),
        ("Pharmacy POS", "Isoko Pharma", "1.8M", "Won"),
    ],
    "system-inventory.html": [
        ("SUGAR-5", "A-03", "6", "Reorder"),
        ("MAIZ-50", "D-08", "210", "OK"),
        ("DETER-2L", "B-11", "0", "Out"),
    ],
    "system-booking.html": [
        ("11:15", "Grace I.", "Antenatal", "Midwife Aline"),
        ("13:00", "Eric N.", "Dental review", "Dr. Kagabo"),
        ("16:30", "Divine U.", "Vaccination", "Nurse Keza"),
    ],
    "system-helpdesk.html": [
        ("#1029", "MoMo refund not received", "Urgent", "18m left"),
        ("#1024", "Cannot print receipt", "Medium", "OK"),
        ("#1017", "Add second user login", "Low", "OK"),
    ],
    "system-lms.html": [
        ("Customer Service Basics", "Apr", "94%", "Completed"),
        ("Bookkeeping for SMEs", "May", "38%", "Live"),
        ("Solar Installation L1", "Jun", "6%", "Starting"),
    ],
    "system-project.html": [
        ("Agaseke e-shop", "Agaseke Co-op", "18 Oct", "OK"),
        ("Clinic EMR pilot", "Remera Health", "2 Oct", "At risk"),
        ("School fees portal", "ES Kicukiro", "24 Oct", "OK"),
    ],
    "system-restaurant-pos.html": [
        ("T2", "Divine", "4", "Ordered"),
        ("T7", "Eric", "5", "Cooking"),
        ("T15", "Keza", "2", "Paid"),
    ],
    "system-bar.html": [
        ("B4", "Regular", "12k", "Open"),
        ("VIP-2", "Corporate", "240k", "Open"),
        ("T21", "Walk-in", "8k", "Settling"),
    ],
    "system-spa.html": [
        ("10:00", "Aline", "Deep tissue 60m", "Keza"),
        ("13:30", "Grace", "Mani + pedi", "Divine"),
        ("17:00", "Sandrine", "Aroma 90m", "Ineza"),
    ],
    "system-gym.html": [
        ("Divine U.", "Silver", "09:22", "OK"),
        ("Eric N.", "Day pass", "10:05", "Guest"),
        ("Grace I.", "Gold", "11:48", "Overdue"),
    ],
    "system-church.html": [
        ("10 Sep", "Tithe", "15,000", "MoMo"),
        ("9 Sep", "Youth fund", "5,000", "MoMo"),
        ("8 Sep", "Widows care", "30,000", "Bank"),
    ],
    "system-ngo.html": [
        ("Water & sanitation", "WaterAid", "36M", "On track"),
        ("Women agri coops", "UN Women", "19M", "Delayed"),
        ("Digital skills", "GIZ", "27M", "On track"),
    ],
    "system-realestate.html": [
        ("Remera apartment", "Divine", "48M", "Viewing"),
        ("Kibagabonga land", "Eric", "65M", "Qualified"),
        ("Nyamirambo duplex", "Keza", "110M", "Negotiation"),
    ],
    "system-construction.html": [
        ("Kanombe warehouse", "Bosco", "42%", "OK"),
        ("Kigali Heights fit-out", "Aline", "88%", "Snags"),
        ("Rubavu road works", "Jean", "21%", "Watch"),
    ],
    "system-legal.html": [
        ("Land dispute 22/24", "Uwase family", "3 Oct", "Filed"),
        ("Employment claim", "Kigali Foods Ltd", "11 Oct", "Drafting"),
        ("Company registration", "Hillside Tech", "—", "Closed"),
    ],
    "system-accounting.html": [
        ("INV-0142", "Nyagatare Traders", "1.2M", "Paid"),
        ("INV-0139", "Kivu Freight", "860k", "Overdue"),
        ("INV-0136", "Umuganda NGO", "2.4M", "Sent"),
    ],
    "system-invoicing.html": [
        ("Q-0087", "Safi Logistics", "4.2M", "Sent"),
        ("Q-0084", "Green Hills Café", "640k", "Accepted"),
        ("Q-0081", "Kivu Marine", "1.9M", "Draft"),
    ],
    "system-field.html": [
        ("Router down — Kimironko", "Ishimwe Ltd", "Eric", "On site"),
        ("CCTV add 4 cams", "Hotel Des Mille", "Bosco", "Scheduled"),
        ("Fibre splice fault", "NetPulse", "Keza", "Overdue"),
    ],
    "system-maintenance.html": [
        ("WO-2211", "Chiller 02", "High", "Open"),
        ("WO-2209", "Generator A", "Medium", "In progress"),
        ("WO-2204", "Boiler valve", "Low", "Closed"),
    ],
    "system-energy.html": [
        ("Kicukiro market", "412", "54%", "OK"),
        ("Nyagatare clinic", "96", "88%", "OK"),
        ("Gisenyi cold store", "640", "22%", "Grid"),
    ],
    "system-water.html": [
        ("W-8842", "Kimihurura", "18", "Paid"),
        ("W-8839", "Nyarutarama", "42", "Due"),
        ("W-8810", "Gikondo", "7", "Dispute"),
    ],
    "system-isp.html": [
        ("Uwase Trading", "Business 50M", "Online", "2m ago"),
        ("Hotel Ihema", "Business 100M", "Online", "live"),
        ("J. Habimana", "Home 20M", "Offline", "6h ago"),
    ],
    "system-school-fees.html": [
        ("Kevin M.", "S3 B", "42,000", "Part paid"),
        ("Aline U.", "S5 A", "0", "Cleared"),
        ("Eric N.", "S2 C", "118,000", "Arrears"),
    ],
    "system-exam.html": [
        ("S4", "Mathematics", "46", "71.2"),
        ("S4", "Biology", "44", "64.8"),
        ("S6", "Entrepreneurship", "38", "77.5"),
    ],
    "system-library.html": [
        ("Things Fall Apart", "S4 B — Kevin", "18 Sep", "On loan"),
        ("Rwanda: History & Society", "T. Aline", "12 Sep", "Overdue"),
        ("Clean Code", "J. Bosco", "24 Sep", "On loan"),
    ],
    "system-hostel.html": [
        ("B-12", "Eric N.", "Occupied", "Back Sun"),
        ("B-14", "Kevin M.", "Occupied", "—"),
        ("C-02", "—", "Vacant", "—"),
    ],
    "system-clinic-emr.html": [
        ("09:40", "Jean B.", "Malaria review", "Seen"),
        ("10:15", "Claire U.", "ANC visit", "Waiting"),
        ("11:00", "Samuel N.", "Chest pain", "Triage"),
    ],
    "system-lab.html": [
        ("S-4412", "Full blood count", "52m", "Resulted"),
        ("S-4409", "HbA1c", "3h 10m", "Running"),
        ("S-4402", "Blood group", "25m", "Resulted"),
    ],
    "system-bloodbank.html": [
        ("U-2214", "A+", "10 Sep", "Available"),
        ("U-2208", "O-", "9 Sep", "Reserved"),
        ("U-2196", "B+", "6 Sep", "Expiring"),
    ],
    "system-insurance.html": [
        ("CL-8842", "Motor — collision", "1.4M", "Assessment"),
        ("CL-8836", "Health — inpatient", "620k", "Approved"),
        ("CL-8821", "Fire — shop", "8.2M", "Investigation"),
    ],
    "system-microfinance.html": [
        ("Twiyunge A", "Keza", "18 Sep", "1.2%"),
        ("Duterimbere", "Bosco", "20 Sep", "0.0%"),
        ("Abakundana", "Aline", "15 Sep", "6.8%"),
    ],
    "system-savings.html": [
        ("Claire U.", "18", "40,000", "Repaying"),
        ("Samuel N.", "12", "—", "Active"),
        ("Divine M.", "24", "85,000", "Overdue"),
    ],
    "system-payroll-sme.html": [
        ("A. Uwase", "380,000", "322,400", "Bank"),
        ("J. Mugabo", "260,000", "224,900", "MoMo"),
        ("C. Ineza", "450,000", "377,100", "Bank"),
    ],
    "system-attendance.html": [
        ("A. Uwase", "07:52", "17:04", "OK"),
        ("J. Mugabo", "08:26", "—", "Late"),
        ("C. Ineza", "07:44", "19:12", "OT"),
    ],
    "system-recruit.html": [
        ("Field technician", "Interview", "6", "Keza"),
        ("Sales agent", "Screening", "22", "Bosco"),
        ("Accountant", "Offer", "1", "Aline"),
    ],
    "system-visitor.html": [
        ("P. Nshuti", "Procurement", "09:12", "V-441"),
        ("SIFA Ltd courier", "Stores", "10:02", "V-447"),
        ("Dr. A. Kagabo", "CEO office", "10:40", "V-451"),
    ],
    "system-assets.html": [
        ("AST-1188", "Dell Latitude 5420", "J. Mugabo", "In use"),
        ("AST-1174", "Projector Epson", "Meeting Rm 2", "In use"),
        ("AST-1160", "Office chair", "—", "Unassigned"),
    ],
    "system-documents.html": [
        ("Board minutes Q3", "Company secretary", "v3", "Approved"),
        ("Lease — Kigali HQ", "Admin", "v2", "Pending"),
        ("Tax clearance 2026", "Finance", "v1", "Archived"),
    ],
    "system-contracts.html": [
        ("Fuel supply", "Kigali Petroleum", "31 Dec", "Renew"),
        ("Security services", "Ishimwe Security", "30 Nov", "Review"),
        ("Software licence", "Hillbot", "15 Oct", "Obligation"),
    ],
    "system-procurement.html": [
        ("RFQ-0142 — Office paper", "Stationery", "5", "Evaluating"),
        ("RFQ-0139 — Fuel Q4", "Energy", "3", "Awarded"),
        ("RFQ-0135 — Laptops (12)", "IT", "7", "Open"),
    ],
    "system-warehouse-retail.html": [
        ("Kimironko", "3.4M", "0.8%", "OK"),
        ("Nyarutarama", "2.1M", "1.6%", "Watch"),
        ("Musanze", "1.2M", "0.4%", "OK"),
    ],
    "system-ecommerce-admin.html": [
        ("#7741", "Claire U.", "48,500", "Packed"),
        ("#7738", "Eric N.", "12,000", "Payment failed"),
        ("#7735", "Divine M.", "126,400", "Delivered"),
    ],
    "system-delivery.html": [
        ("Kevin", "Nyarutarama", "6", "Delivering"),
        ("Aline", "Gikondo", "4", "At hub"),
        ("Samuel", "Musanze", "9", "Returning"),
    ],
    "system-taxi.html": [
        ("J-2214", "Remera → CBD", "Bosco", "On trip"),
        ("J-2210", "Airport → Kiyovu", "Eric", "Assigned"),
        ("J-2207", "Nyamirambo → CHUK", "Keza", "Completed"),
    ],
    "system-parking.html": [
        ("A-12", "RAD 442K", "08:14", "Occupied"),
        ("B-04", "RAC 118T", "09:02", "Occupied"),
        ("C-19", "—", "—", "Free"),
    ],
    "system-events-ticketing.html": [
        ("Regular", "5,000", "820", "180"),
        ("Table of 6", "60,000", "24", "6"),
        ("Student", "2,500", "310", "90"),
    ],
    "system-membership.html": [
        ("Grace I.", "Family", "12,000", "Overdue"),
        ("Bosco N.", "Corporate", "0", "Active"),
        ("Claire U.", "Individual", "0", "Renewing"),
    ],
    "system-agri.html": [
        ("Plot 4 — Nyamata", "Maize", "Flowering", "OK"),
        ("Plot 7 — Bugesera", "Beans", "Vegetative", "Pest alert"),
        ("Plot 2 — Kanombe", "Tomato", "Harvest", "OK"),
    ],
    "system-coop.html": [
        ("J. Habimana", "Maize", "420", "Paid"),
        ("M. Uwimana", "Coffee cherry", "180", "Queued"),
        ("A. Nsengiyumva", "Beans", "260", "Paid"),
    ],
    "system-vet.html": [
        ("RW-4412", "Friesian", "Milking", "12 Oct"),
        ("RW-4408", "Jersey", "Dry", "2 Nov"),
        ("RW-4390", "Friesian", "Calf", "28 Sep"),
    ],
    "system-coldchain.html": [
        ("Vaccine store A", "+4.2°C", "2–8°C", "OK"),
        ("Cold room 2", "-19.4°C", "-22 to -18", "OK"),
        ("Van RW-221", "+7.8°C", "2–8°C", "Alert"),
    ],
    "system-quality.html": [
        ("NC-0142", "Packaging line 2", "Major", "CAPA open"),
        ("NC-0139", "Labelling", "Minor", "Closed"),
        ("NC-0135", "Raw goods in", "Major", "Investigating"),
    ],
    "system-hse.html": [
        ("PTW-0142", "Hot work", "Boiler room", "Open"),
        ("PTW-0140", "Confined space", "Tank 3", "Closed"),
        ("PTW-0138", "Working at height", "Roof east", "Open"),
    ],
    "system-helpdesk-it.html": [
        ("IT-2214", "VPN keeps dropping", "P2", "Assigned"),
        ("IT-2211", "New starter laptop", "P3", "In progress"),
        ("IT-2205", "Email sync iOS", "P4", "Resolved"),
    ],
    "system-chatbot.html": [
        ("WhatsApp", "Claire U.", "Order status", "Bot"),
        ("Web chat", "Eric N.", "Pricing", "Human"),
        ("Instagram DM", "Divine M.", "Booking", "Bot"),
    ],
    "system-survey.html": [
        ("After purchase", "62", "214", "Up"),
        ("Support close", "41", "186", "Flat"),
        ("In-store exit", "55", "212", "Up"),
    ],
    "system-loyalty.html": [
        ("Grace I.", "Gold", "2,480", "2 days ago"),
        ("Samuel N.", "Silver", "910", "1 week ago"),
        ("Divine M.", "Bronze", "240", "3 weeks ago"),
    ],
    "system-subscription.html": [
        ("Kivu Coffee", "Business", "1 Oct", "Active"),
        ("J. Mugabo", "Starter", "22 Sep", "Past due"),
        ("Safi Ltd", "Enterprise", "5 Oct", "Active"),
    ],
    "system-analytics.html": [
        ("Sales performance", "Finance", "08:00", "Fresh"),
        ("Customer churn", "Growth", "08:00", "Fresh"),
        ("Stock cover", "Ops", "06:30", "Alert"),
    ],
    "system-kiosk.html": [
        ("Q-118", "Cashier 2", "4m", "Waiting"),
        ("Q-117", "Advisory", "1m", "Serving"),
        ("Q-114", "Cashier 1", "—", "Done"),
    ],
}
