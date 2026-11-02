from datetime import datetime,timedelta
import connector as c 
def display_tour_details():
    sql = 'select id, title, detail, start_date, days from tour_details where is_deleted = 0 order by id'
    tour_details = c.fetchData(sql)
    print(f"{'id':<5} {'title':<25} {'detail':<35} {'start_date':<20} {'days':<5}")
    print("-" * 110)
    for index, row in enumerate(tour_details):
        print(f"{str(row['id']):<5} {str(row['title']):<25} {str(row['detail']):<35} {str(row['start_date']):<20} {str(row['days']):<5}")
        if (index+1) % 10 == 0:
            key = input("Press any key to continue")

def display_transcations():
    sql = 'select tourid,amount,chalan_no,transcation_dt from transcations where is_deleted = 0 order by tourid'
    transcations = c.fetchData(sql)
    print(f"{'tourid':<10} {'amount':<15} {'chalan_no':<20} {'transcation_dt':<20}")
    print('-' * 110)
    for index, row in enumerate(transcations):
        print(f"{str(row['tourid']):<10} {str(row['amount']):<15} {str(row['chalan_no']):<20} {str(row['transcation_dt']):<20}")

        if (index+1) % 10 == 0 and (index+1) < len(transcations):
            key = input("Press any key to continue")

while True:
    print('press 1 for tour management')
    print('press 2 for transaction management')
    print('press 3 for report management')
    print('press 0 for exit')
    choice = int(input('enter your choice: '))
    if choice == 1:
        while True:
            print('-' * 110)
            print('tour management')
            print('-' * 110)
            print('press 1 for insert ')
            print('press 2 for update ')
            print('press 3 for delete ')
            print('press 4 for view ')
            print('press 0 for exit ')
            tour_man_choice = int(input('enter your choice: '))
            if tour_man_choice == 1:
                title = input('enter a title: ')
                detail = input('enter a detail: ')
                start_date = int(input('enter start_date'))
                days = int(input('enter days: '))
                adult_rate = int(input('enter a adult rate'))
                child_rate = int(input('enter a child rate'))
                sql = 'insert into tour_details (title,detail,start_date,days,adult_rate,child_rate) values  (%s,%s,%s,%s,%s,%s)'
                values = [title,detail,start_date,days,adult_rate,child_rate]
                success = c.runSQL(sql,values)
                if success == 1:
                    print('tour_details added successfully')
                    key = ('press any key to continue')

            elif tour_man_choice == 2:
                display_tour_details()
                id = int(input('enter a id to update a tour'))
                sql = 'select id from tour_details where id = %s'
                values = [id]
                tour_details = c.fetchData(sql,values)
                if len(tour_details) == 0:
                    print('no product found')
                else:
                    title = input('enter a title: ')
                    detail = input('enter a title: ')
                    start_date = int(input('enter start_date'))
                    days = int(input('enter days: '))
                    adult_rate = int(input('enter a adult rate'))
                    child_rate = int(input('enter a child rate'))
                    sql = 'update tour_details set title = %s,details = %s,start_date = %s,days = %s,adult_rate = %s,child_rate = %s where id = %s'
                    values =  [title,detail,start_date,days,adult_rate,child_rate,id]
                    success = c.runSQL(sql,values)
                    if success == 1:
                        print(' your tour_details is updated successfully')
                        key = ('press any number to continue')

            elif tour_man_choice == 3:
                display_tour_details()
                id = int(input("enter tour id to delete"))
                sql = "update product set is_deleted = 1 where id = %s"
                values = [id]
                if success == 1:
                    print("tour_details has been deleted")

            elif tour_man_choice == 4:
                display_tour_details()

            elif tour_man_choice == 0:
                print('let us return to main menu')
                break
            else:
                print('not valid choice') 

    elif choice == 2:
        while True:
            print('-' * 110)
            print('transcation management')
            print('-' * 110)
            print('press 1 for insert in transcation management')
            print('press 2 for view in transcation management')
            print('press 3 for delete in transcation management ')
            print('press 4 for search in transcation management ')
            print('press 0 for exit ')  
            tran_man_choice = int(input('enter your choice: '))
            if tran_man_choice == 1:
                tourid = int(input('enter a tourid '))
                amount = int(input('enter a amount'))
                chalan_no = int(input('enter a chalan_no'))
                transcation_dt = int(input('enter a transcation date'))
                sql = 'insert into transcations (tourid,amount,chalan_no,transcation_dt) values  (%s,%s,%s,%s)'
                values = [tourid,amount,chalan_no,transcation_dt]
                success = c.runSQL(sql,values)
                if success == 1:
                    print('transcations added successfully')
                    key = ('press any key to continue')

            elif tran_man_choice == 2:
                display_transcations()

            elif tran_man_choice == 3:
                display_tour_details()
                id = int(input("enter tour id to delete"))

                sql = "update tour_detail set is_deleted = 1 where id = %s"
                values = [id]
                success = c.runSQL(sql, values)

                if success == 1:
                    print("tour_details has been deleted")

            elif tran_man_choice == 4:
                search_value = input('enter tourid for search ')

                sql = "select tourid, amount, chalan_no, transcation_dt from transcations where tourid = %s and is_deleted = 0 order by tourid"
                values = [search_value]
                transcations = c.fetchData(sql, values)

                print(f"{'tourid':<10} {'amount':<15} {'chalan_no':<20} {'transcation_dt':<20}")
                print("-" * 80)

                if len(transcations) == 0:
                    print("No tourid found")
                else:
                    for index, row in enumerate(transcations):
                        print(f"{str(row['tourid']):<10} {str(row['amount']):<15} {str(row['chalan_no']):<20} {str(row['transcation_dt']):<20}")

                        if (index+1) % 10 == 0 and (index+1) < len(transcations):
                            key = input("Press any key to continue")

                key = input("Press any key to continue")


            elif tran_man_choice == 0:
                print('let us return to main menu')
                break
            else:
                print('not valid choice') 
    elif choice == 3:
        while True:
            print('-' * 110)
            print('report management')
            print('-' * 110)
            print('press 1 for month wise income expense report ')
            print('press 2 for quarter wise income expense report')
            print('press 3 for year wise income expense report ')
            print('press 4 for tour wise income expense report (tour id will be given by user) ')
            print('press 5 for tour wise income expense report (all tour)')
            print('press 0 for exit ')  
            report_choice = int(input('enter your choice: '))
            if report_choice == 1:
                year = int(input('Enter year: '))
                month = int(input('Enter month (1-12): '))
                sql = "SELECT tourid, amount, description, chalan_no, transcation_dt FROM transcations WHERE is_deleted = 0 AND YEAR(transcation_dt) = %s AND MONTH(transcation_dt) = %s"
                values = [year, month]
                transcations = c.fetchData(sql, values)
                
                sql = "SELECT SUM(amount) AS income from transcations where is_deleted = 0and YEAR(transcation_dt) = %s AND MONTH(transcation_dt) = %s"
                values = [year, month]
                income_result = c.fetchData(sql, values)

                total_income =( income_result[0]['income']
                    if income_result and income_result[0]['income'] is not None
                    else 0)
                
                print(f"{'tourid':<10} {'amount':<15} {'chalan_no':<20} {'transcation_dt':<20}")
                print('-' * 110)

                for index, row in enumerate(transcations):
                    print(f"{str(row['tourid']):<10} "
                        f"{str(row['amount']):<15} "
                        f"{str(row['chalan_no']):<20} "
                        f"{str(row['transcation_dt']):<20}")  
                if (index + 1) % 10 == 0 and (index + 1) < len(transcations):
                        input("Press Enter to continue...")
                print('-' * 110)
                print(f"Total income for {month}/{year}: {total_income}")
                        

            elif report_choice == 2:
                year = int(input('Enter year: '))
                quarter = int(input('Enter quarter (1-4): '))

                start_month = (quarter - 1) * 3 + 1
                end_month = start_month + 2

                if quarter not in [1, 2, 3, 4]:
                    print("Invalid quarter!")
                else:
                    sql = "select tourid, amount, description, chalan_no, transcation_dt from transcations where is_deleted = 0 and year(transcation_dt) = %s and month(transcation_dt) BETWEEN %s AND %s"
                    values = [year, start_month, end_month]
                    transcations = c.fetchData(sql, values)

                    sql = "select SUM(amount) as income from transcations where is_deleted = 0 and year(transcation_dt) = %s and month(transcation_dt) BETWEEN %s AND %s and amount > 0"
                    income_result = c.fetchData(sql, values)
                    total_income = income_result[0]['income'] or 0

                    sql = "select SUM(ABS(amount)) as expense from transcations where is_deleted = 0 and year(transcation_dt) = %s and month(transcation_dt) BETWEEN %s AND %s and amount < 0"
                    expense_result = c.fetchData(sql, values)
                    total_expense = expense_result[0]['expense'] or 0

                    print(f"{'tourid':<10} {'amount':<15} {'chalan_no':<20} {'transcation_dt':<20}")
                    print('-' * 110)

                    for index, row in enumerate(transcations):
                        print(f"{str(row['tourid']):<10} {str(row['amount']):<15} {str(row['chalan_no']):<20} {str(row['transcation_dt']):<20}")

                        if (index + 1) % 10 == 0 and (index + 1) < len(transcations):
                            input("Press Enter to continue...")
            elif report_choice == 3:
                year = int(input('Enter year: '))

                sql = "SELECT tourid, amount, description, chalan_no, transcation_dt FROM transcations WHERE is_deleted = 0 AND YEAR(transcation_dt) = %s"
                values = [year]
                transcations = c.fetchData(sql, values)

                sql = "SELECT SUM(amount) AS income FROM transcations WHERE is_deleted = 0 AND YEAR(transcation_dt) = %s AND amount > 0"
                income_result = c.fetchData(sql, values)
                total_income = income_result[0]['income'] or 0

                sql = "SELECT SUM(ABS(amount)) AS expense FROM transcations WHERE is_deleted = 0 AND YEAR(transcation_dt) = %s AND amount < 0"
                expense_result = c.fetchData(sql, values)
                total_expense = expense_result[0]['expense'] or 0

                print(f"{'tourid':<10} {'amount':<15} {'chalan_no':<20} {'transcation_dt':<20}")
                print('-' * 110)

                for index, row in enumerate(transcations):
                    print(f"{str(row['tourid']):<10} {str(row['amount']):<15} {str(row['chalan_no']):<20} {str(row['transcation_dt']):<20}")

                    if (index + 1) % 10 == 0 and (index + 1) < len(transcations):
                        input("Press Enter to continue...")

                print('-' * 110)
                print(f"Total income for {year}: {total_income}")
                print(f"Total expense for {year}: {total_expense}")
                print(f"Net balance: {total_income - total_expense}")


            elif report_choice == 4:
                tourid = int(input('Enter tour ID: '))

                sql = "SELECT tourid, amount, description, chalan_no, transcation_dt FROM transcations WHERE is_deleted = 0 AND tourid = %s"
                values = [tourid]
                transcations = c.fetchData(sql, values)

                sql = "SELECT SUM(amount) AS income FROM transcations WHERE is_deleted = 0 AND tourid = %s AND amount > 0"
                income_result = c.fetchData(sql, values)
                total_income = income_result[0]['income'] or 0

                sql = "SELECT SUM(ABS(amount)) AS expense FROM transcations WHERE is_deleted = 0 AND tourid = %s AND amount < 0"
                expense_result = c.fetchData(sql, values)
                total_expense = expense_result[0]['expense'] or 0

                print(f"{'tourid':<10} {'amount':<15} {'chalan_no':<20} {'transcation_dt':<20}")
                print('-' * 110)

                for index, row in enumerate(transcations):
                    print(f"{str(row['tourid']):<10} {str(row['amount']):<15} {str(row['chalan_no']):<20} {str(row['transcation_dt']):<20}")

                    if (index + 1) % 10 == 0 and (index + 1) < len(transcations):
                        input("Press Enter to continue...")

                print('-' * 110)
                print(f"Total income for tour {tourid}: {total_income}")
                print(f"Total expense for tour {tourid}: {total_expense}")
                print(f"Net balance: {total_income - total_expense}")
            elif report_choice == 0:
                print('let us return to main menu')
                break
            else:
                print('not valid choice')
    elif choice == 0:
        print("thank you for using our software, have a good day")
        break 
    else:
        print("not a valid choice")

    
 