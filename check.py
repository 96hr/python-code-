class RestaurantCheck:
    def __init__(self, check_number, sales_tax_percent, subtotal, table_number, server_name):
        self.check_number = check_number
        self.sales_tax_percent = sales_tax_percent
        self.subtotal = subtotal
        self.table_number = table_number
        self.server_name = server_name
    
    def calculate_total(self):
        sales_tax_amount = self.subtotal * (self.sales_tax_percent / 100)
        total = self.subtotal + sales_tax_amount
        return total
    
    def print_check(self):
        filename = f"check{self.check_number}.txt"
        
        total = self.calculate_total()
        
        content = f"Check Number: {self.check_number}\n"
        content += f"Sales tax: {self.sales_tax_percent}%\n"
        content += f"Subtotal: ${self.subtotal:.2f}\n"
        content += f"Total: ${total:.2f}\n"
        content += f"Table Number: {self.table_number}\n"
        content += f"Server: {self.server_name}\n"
        
        with open(filename, 'w') as file:
            file.write(content)
        
        print(f"Check details have been saved to {filename}")
