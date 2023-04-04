import React from 'react';
import ExpenseForm from './ExpenseForm';
import './NewExpense.css';

function NewExpense (props) {

  function saveDataHandler (saveData) {
    const expenseData = {
      ...saveData,
      id: Math.random().toString()
    }
    props.onGetData(expenseData)
  }

  return (
    <div className='new-expense'>
      <ExpenseForm onSaveData={saveDataHandler}></ExpenseForm>
    </div>
  )

}

export default NewExpense;