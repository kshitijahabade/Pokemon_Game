// Move list and damage (replace with your desired moves and damage)
const moveList = ["Tackle", "Ember", "Vine Whip", "Water Gun"];
const damageDealt = [5, 8, 7, 10];

let enemyPokemon; // To store the encountered Pokemon
let yourHealth = 100; // Your Pokemon's health

function startBattle() {
  enemyPokemon = moveList[Math.floor(Math.random() * moveList.length)]; // Choose random Pokemon
  document.getElementById("enemy-pokemon").innerText = `Wild ${enemyPokemon} appeared!`;
  updateHealthBar();
  displayMoveSelection();
}

function updateHealthBar() {
  document.getElementById("your-health").innerText = yourHealth;
}

function displayMoveSelection() {
  let moveSelection = "";
  for (let i = 0; i < moveList.length; i++) {
    moveSelection += `<button onclick="attack(${i})">${moveList[i]}</button>`;
  }
  document.getElementById("move-selection").innerHTML = moveSelection;
}

function attack(moveIndex) {
  const enemyMove = moveList[Math.floor(Math.random() * moveList.length)];
  const enemyDamage = Math.floor(Math.random() * damageDealt[enemyMove]);
  const yourDamage = Math.floor(Math.random() * damageDealt[moveIndex]);

  // Update battle log
  const battleLog = document.getElementById("battle-log");
  battleLog.innerText = `You used ${moveList[moveIndex]}! Enemy ${enemyPokemon} used ${enemyMove}!\n`;
  battleLog.innerText += `You dealt ${yourDamage} damage. Enemy dealt ${enemyDamage} damage.\n`;

  // Update health
  yourHealth -= enemyDamage;
  enemyHealth -= yourDamage; // Simulate enemy health (not shown)

  updateHealthBar();

  // Check win/lose condition (replace with desired logic)
  if (yourHealth <= 0) {
    battleLog.innerText += "You fainted! Game Over!";
  } else if (enemyHealth <= 0) {
    battleLog.innerText += "You won the battle!";
    // Add logic for catching/winning (not implemented here)
  } else {
    displayMoveSelection(); // Continue battle
  }
}

startBattle();
