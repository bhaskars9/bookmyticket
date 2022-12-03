// const container = document.querySelector('.container');
// const seats = document.querySelectorAll('.row .seat:not(.occupied)');
// const count = document.getElementById('count');
// const total = document.getElementById('total');
// const movieSelect = document.getElementById('movie');

// let ticketPrice = +movieSelect.value;

// // update total and count
// function updateSelectedCount() {
//   const selectedSeats = document.querySelectorAll('.row .seat.selected')
//   ;
  
//   // Copy selected seats into array
//   // Map through array
//   // Return new array indexes
  
//   const seatsIndex = [...selectedSeats].map(seat => [...seats].indexOf(seat));
  
//   localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));

//   const selectedSeatsCount = selectedSeats.length;
  
//   count.innerText = selectedSeatsCount;
//   total.innerText = selectedSeatsCount * ticketPrice;
// }

// // movie slect event
// movieSelect.addEventListener('change', e => {
//   ticketPrice = e.target.value;
//   updateSelectedCount();
// })

// // seat click event
// container.addEventListener('click', e => {
//   if(e.target.classList.contains('seat') && 
//      !e.target.classList.contains('occupied')
//     ) {
//     e.target.classList.toggle('selected');
    
//     updateSelectedCount();
//   }
// })

