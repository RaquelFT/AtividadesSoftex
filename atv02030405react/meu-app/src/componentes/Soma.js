import React,{useState} from 'react'

export default function Soma(){

    const[num, setNum]=useState(10)

    return(
        <>
            <p>Valor do state num: {num}</p>
            <button onClick={()=>setNum(num+10)}>Soma 10</button>
        </>    
    )
}