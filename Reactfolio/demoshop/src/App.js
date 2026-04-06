import logo from './logo.svg';
import './App.css';
import Item from './components/Item';
import ItemDate from './components/ItemDate';

function App() {
  const response = [
  {
    itemName : "Nirma",
    itemDate : "20",
    itemMonth : "June",
    itemyear : "1998"
  },
  {
    itemName : "SurfExcel",
    itemDate : "22",
    itemMonth : "July",
    itemyear : "1999"
  },
  {
    itemName : "Rin",
    itemDate : "24",
    itemMonth : "August",
    itemyear : "2000"
  }
];
  return (
    <div>
      <Item name={response[0].itemName}></Item>
        Hello i am your first item
      <ItemDate day={response[0].itemDate} month={response[0].itemMOnth} year={response[0].itemyear}></ItemDate>

      <Item name={response[1].itemName}></Item>
      <ItemDate day={response[1].itemDate} month={response[1].itemMonth} year={response[1].itemyear}></ItemDate>

      <Item name={response[2].itemName}></Item>
      <ItemDate day={response[2].itemDate} month={response[2].itemMonth} year={response[2].itemyear}></ItemDate>
      <div className="App">Hello</div>



    </div>
  );
}

export default App;
