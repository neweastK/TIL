import ExpenseItem from "./ExpenseItem";
import Card from "../UI/Card";
import ExpensesFilter from "./ExpenesesFilter";
import "./Expenses.css";

function Expenses(props) {

  const selectedYearHandler = (selectedYear) => { console.log(selectedYear) }

  return (
    <Card className="expenses">
      <ExpensesFilter onSelectYear={selectedYearHandler}></ExpensesFilter>
      <ExpenseItem
        title={props.items[0].title}
        date={props.items[0].date}
        amount={props.items[0].amount}
      ></ExpenseItem>
      <ExpenseItem
        title={props.items[1].title}
        date={props.items[1].date}
        amount={props.items[1].amount}
      ></ExpenseItem>
      <ExpenseItem
        title={props.items[2].title}
        date={props.items[2].date}
        amount={props.items[2].amount}
      ></ExpenseItem>
      <ExpenseItem
        title={props.items[3].title}
        date={props.items[3].date}
        amount={props.items[3].amount}
      ></ExpenseItem>
    </Card>
  );
}

export default Expenses;
