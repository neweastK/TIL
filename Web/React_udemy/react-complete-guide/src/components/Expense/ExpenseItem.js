import React, { useState } from 'react';
import ExpenseDate from './ExpenseDate';
import Card from '../UI/Card';
import './ExpenseItem.css';

function ExpenseItem (props) {

  const [title,setTitle] = useState(props.title)
  console.log(props.title)

  function clickHandeler () {
    setTitle("changed!!")
    console.log("변함")
  }

  return (
    <Card className='expense-item'>
      <ExpenseDate date={props.date}></ExpenseDate>
      <div className='expense-item__description'>
        <h2>{title}</h2>
        <div className='expense-item__price'>${props.amount}</div>
      </div>
      <button onClick={clickHandeler}>change setting</button>
    </Card>
  )
}

export default ExpenseItem;