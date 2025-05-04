// Duration of your trace, in milliseconds
let shnata = 2.61999*3 // 3 iterations

// Array of length TRACE_LENGTH with your trace's values
let BUFFER_SIZE = 8192;

// Value of performance.now() when you started recording your trace
let start;

function record() {
  // Create empty array for saving trace values
  T = new Array(100);

  // Fill array with -1 so we can be sure memory is allocated
  T.fill(-1, 0, T.length);


  // Save start timestamp
  const LINE_SIZE = 16;
  const buffer_memory = new Array(64 * LINE_SIZE).fill(-1);
  console.log(T)
  
  for(let i=0; i<100; i++){
    start = performance.now();
    end = start + shnata;
    let loop_iterations = 0;
    while(start <= end){
      //read bytes from cache
      for (let j = 0; j < BUFFER_SIZE; j++) {
        let val = buffer_memory[j * LINE_SIZE];
      }
      start = performance.now();
      loop_iterations ++;
    }
    T[i] = loop_iterations;
    loop_iterations = 0;

  }
  console.log(T)

  // Once done recording, send result to main thread
  postMessage(JSON.stringify(T));
}

// DO NOT MODIFY BELOW THIS LINE -- PROVIDED BY COURSE STAFF
self.onmessage = (e) => {
  if (e.data.type === "start") {
    TRACE_LENGTH = e.data.trace_length;
    setTimeout(record, 0);
  }
};
