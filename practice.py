import itertools

class Category:
  def __init__(self, name=""):
    self.name = name
    self.balance = 0
    self.ledger = []

  def __str__(self):
    title = "{:*^30}".format(self.name)
    lines = ""
    for i in self.ledger:
      lines += "{description:<23.23s}{amount:>7.2f}\n".format(**i, width = 30)
      #for key, value in i.items():
        #lines += "{:<23}{:>7}".format(key['description'], ['amount'])
      
    return f"{title}\n{lines}Total: {self.balance:.2f}"
    #return f"{self.name}\n{self.ledger}\nTotal: {self.balance}"

  def deposit(self, amount, description=""):
    self.balance += amount
    deposit = {"amount": amount, "description": description}
    self.ledger.append(deposit)


  def withdraw(self, amount, description=""):
    if self.check_funds(amount) is True:
      self.balance += -amount
      withdrawal = {"amount": -amount, "description": description}
      self.ledger.append(withdrawal)
      return True
    else:
      return False

  def get_balance(self):
    return round(self.balance, 2)

  def transfer(self, amount, category):
    description_to = "Transfer to " + category.name
    description_from = "Transfer from " + self.name
    if self.check_funds(amount) is True:
      self.balance += -amount
      transfer_from = {"amount": -amount, "description": description_to}
      self.ledger.append(transfer_from)
      category.balance += amount
      transfer_to = {"amount": amount, "description": description_from}
      category.ledger.append(transfer_to)
      return True
    else:
      return False
    

  def check_funds(self, amount):
    return self.balance >= amount


  

"""
def chart(digits,catnames):
  rows = 100
  bar_graph = []
  total_line = '---'*(len(digits)+1)
  chart_list = ['100|',' 90|', ' 80|',' 70|', ' 60|',' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
  chart = ""
  #print("Percentage spent by category")
  #for row in range(rows, -1, -10):
    #return(row,'|',' '.join(['o' if digit >= row else ' ' for digit in digits]))
  for row in range(rows, -1, -10):
    bar_graph.append(['o' if digit >= row else ' ' for digit in digits])

  return bar_graph
  #for row, mark in zip(bar_graph, chart_list):
    #print(mark,'  '.join(row))
  line_space = len(total_line) + 4
  print(f"{total_line:>{line_space}}")
  for i in itertools.zip_longest(*catnames, fillvalue=' '):
    if any(j != ' ' for j in i):
      print('    ','  '.join(i))
   
  #for name in cat_labels:
    #print(name,'\n')
  
"""  

def create_spend_chart(categories):
  totals = {}
  totals_by_cat = []
  #total = 0
  grand_total = 0
  percents = []
  total_line = '---'*(len(categories))
  cat_names = []
  num_bars = []
  chart_list = ['100|',' 90|', ' 80|',' 70|', ' 60|',' 50|', ' 40|', ' 30|', ' 20|', ' 10|']
  
  chart = 'Percentage spent by category\n'
  

  # for each category in list
  for cat in categories:
    ledger = cat.ledger
    total = 0
    #print(f"ledger: {ledger}")
    # for each expense in ledger, if negative update running total per category
    for expense in ledger:
      if expense['amount'] < 0:
        total += abs((expense['amount']))
        totals_by_cat.append(total)
        #print(f"total: {total}")
        grand_total += total
    #print(f"total:{total}")
    #print(f"grand total:{grand_total}")
    # add category names to cat_names list
    cat_names.append(cat.name)

    # add category name, total withdrawals to totals dict
    totals[cat.name] = total
  
    # get percents by category and append to percents list
  for totals in totals_by_cat:
    percent = round(totals/grand_total, 3)
    percents.append(percent)
    #print(f"percent loop: {percent}")
    #percents.append(round(*totals_by_cat/grand_total, 2))
    #print(f"percents:{percents}")
   

    

  # determine number of 'o' needed per category, append number to num_bars list
  for i in percents:
    bubbles = i//.01
    num_bars.append(int(bubbles))

  
    
  for number in range(100, -10, -10):
    chart += f"{number:3d}| "
    for percent in num_bars:
      if percent >= number:
        chart += 'o  '
      else:
        chart += '   '

    chart += '\n'
  #get_chart = chart(num_bars, cat_names)

  #for row, mark in zip(get_chart, chart_list):
    #chart_str.append(mark + ' '.join(row))
    #print(mark,'  '.join(row))
    #chart_str = mark, '  '.join(row)
  #return ((mark, row) for row, mark in zip(get_chart, chart_list))
  #return(f"Chart_str: {chart_str}")
  # Create horizontal line
  line_space = len(total_line) + 2
  chart += f"  {total_line:>{line_space}}-\n"
  #print(f"{total_line:>{line_space}}")
  # Create vertical category names
  # Create vertical category names
  # Create vertical category names
  line_count = 0
  
  for i in itertools.zip_longest(*cat_names, fillvalue=' '):
    #if any(j != ' ' for j in i):
    cats = '  '.join(i)
    line_count += 1
    chart += f"     {cats}  \n"

  
    
    
    #if line_count < last:
      #chart += "\n"
    #print(line_count)
    #print(last)
        
    #print(i)
    #print(len(cats))
    #print(repr(cats))
    #chart += '\n' if not cats[:-1] else ''


  
  return chart.rstrip('\n')
        

