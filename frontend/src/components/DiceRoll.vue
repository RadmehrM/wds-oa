<template>
  <section class="dice-roller-section">
        <div class="container text-center my-2">
            <div class="header-title h1 mb-5">Dice Roller Game</div>
            <div class="three-column-section">
                <div
                    class="column simulate d-flex align-items-center justify-content-center"
                    @click="rollDice(1)"
                >
                    <img :src="currentDice1" alt="Dice 1" class="img-fluid" />
                </div>
                <div
                    class="column practice d-flex align-items-center justify-content-center"
                    @click="rollDice(2)"
                >
                    <img :src="currentDice2" alt="Dice 2" class="img-fluid" />
                </div>
                <div
                    class="column master d-flex align-items-center justify-content-center"
                    @click="rollDice(3)"
                >
                    <img :src="currentDice3" alt="Dice 3" class="img-fluid" />
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue';
import dice1 from '../../staticfiles/img/dice-1.png';
import dice2 from '../../staticfiles/img/dice-2.png';
import dice3 from '../../staticfiles/img/dice-3.png';
import dice4 from '../../staticfiles/img/dice-4.png';
import dice5 from '../../staticfiles/img/dice-5.png';
import dice6 from '../../staticfiles/img/dice-6.png';

const diceImages = [dice1, dice2, dice3, dice4, dice5, dice6];

const currentDice1 = ref(dice1);
const currentDice2 = ref(dice2);
const currentDice3 = ref(dice3);

let rolling = [false, false, false]; // Prevent double roll
function getRandomDice() {
    const idx = Math.floor(Math.random() * diceImages.length);
    return diceImages[idx];
}

function rollDice(column) {
    const idx = column - 1;
    if (rolling[idx]) return; // Prevent multiple rolls at once
    rolling[idx] = true;

    let interval;
    let count = 0;
    const maxCount = 15 + Math.floor(Math.random() * 10); // Randomize roll duration

    interval = setInterval(() => {
        const randomDice = getRandomDice();
        if (column === 1) currentDice1.value = randomDice;
        if (column === 2) currentDice2.value = randomDice;
        if (column === 3) currentDice3.value = randomDice;
        count++;
        if (count > maxCount) {
            clearInterval(interval);
            // Settle on final value
            const finalDice = getRandomDice();
            if (column === 1) currentDice1.value = finalDice;
            if (column === 2) currentDice2.value = finalDice;
            if (column === 3) currentDice3.value = finalDice;
            rolling[idx] = false;
        }
    }, 60); // Change image every 60ms
}
</script>


<style scoped>

.header-title {
    font-size: 2.5rem;
    font-weight: bold;
    color: white;
    margin-bottom: 2rem;
}

.container {
  max-width: 1200px;
  
}
.three-column-section {
  display: flex;
  flex-wrap: wrap; 
  width: 100%;
  height: auto !important;
}

.three-column-section .column {
  flex: 1;
  padding: 3rem !important;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}


/* Responsive styles */
@media (max-width: 1100px) {
  .three-column-section {
    height: 100vh;
    flex-direction: column;
    height: auto;
  }
  .three-column-section .column {
    width: 100%;
    padding: 2rem;
    align-items: center;
    text-align: center;
    
  }

   .three-column-section .column p {
    font-size: 1.5rem !important;
  }

}
</style>