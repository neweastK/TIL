import React, { useState } from 'react';
import './ExpenseForm.css';

function ExpenseForm (props) {
  const [userInput,setUserInput] = useState({
    enteredTitle: '',
    enteredAmount: '',
    enteredDate: '',
  })
  
  
  function titleChangeHandler (event) {
    setUserInput(function(prevState){
      return {
        ...prevState,
        enteredTitle: event.target.value
      }
    })
  }

  function amountChangeHandler (event) {
    setUserInput(function(prevState){
      return {
        ...prevState,
        enteredAmount: event.target.value
      }
    }
    )}

  function dateChangeHandler (event) {
    setUserInput(function(prevState){
      return {
        ...prevState,
        enteredDate: Date(event.target.value)
      }
    })
  }

  function submintHandler (event) {
    event.preventDefault()

    props.onSaveData(userInput)

    setUserInput(function(){
      return {
        enteredTitle: '',
        enteredAmount: '',
        enteredDate: ''
      }
    })
  }

  return (
      <form onSubmit={submintHandler}>
        <div className='new-expense__controls'>
          <div className='new-expense__control'>
            <label>Title</label>
            <input  
              type='text'
              onChange={titleChangeHandler}
              value={userInput.enteredTitle}
            ></input>
          </div>
          <div className='new-expense__control'>
            <label>Amount</label>
            <input 
              type='number'
              min='0,01'
              step='0.01'
              onChange={amountChangeHandler}
              value={userInput.enteredAmount}
            ></input>
          </div>
          <div className='new-expense__control'>
            <label>Date</label>
            <input 
              type='date'
              min='2019-01-01'
              max='2022-12-31'
              onChange={dateChangeHandler}
              value={userInput.enteredDate}
            ></input>
          </div>
        </div>
        <div className='new-expense__actions'>
          <button type='submit'>Add Expense</button>
        </div>
      </form>
  )
}

export default ExpenseForm;