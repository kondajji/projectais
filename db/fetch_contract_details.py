import sqlite3

DB_PATH = "db/ais.db"

def get_contract_details(vendor_name):
    """Fetch contract details for a given vendor."""
    query = """
    SELECT vendor_name, start_date, end_date, contract_value, invoiced_amount, payment_status, contract_status, renewal_date
    FROM contracts
    WHERE vendor_name = ?;
    """

    print("Vendor Name:", vendor_name)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, (vendor_name,))
    result = cursor.fetchone()
    conn.close()

    if result:
        print("result found")
        vendor, start_date, end_date, value, invoiced, payment_status, status, renewal = result
        return (f"📌 Contract Details for {vendor}:\n"
                f"- Start Date: {start_date}\n"
                f"- End Date: {end_date}\n"
                f"- Contract Value: ${value}\n"
                f"- Invoiced Amount: ${invoiced}\n"
                f"- Payment Status: {payment_status}\n"
                f"- Contract Status: {status}\n"
                f"- Renewal Date: {renewal if renewal else 'No renewal scheduled'}")
    else:
        return f"No contract details found for {vendor_name}."


if __name__ == "__main__":
    vendor = input("Enter Vendor Name: ")
    print(get_contract_details(vendor))
