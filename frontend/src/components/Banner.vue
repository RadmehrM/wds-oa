
<template>

    <div class="banner-cat-wrapper bg-light">
        <div id="index_banner" class="container-fluid p-0">
        <div class="background w-100 h-100">
            <div
            class="banner-text col-lg-4 col-12 d-flex justify-content-center align-items-center p-0"
            >
            <div
                class="banner-content text-left w-75 d-flex justify-content-center align-items-center m-0 pb-5"
            >
                <div class="w-75 p-5 mb-2 pe-0 d-flex flex-column justify-content-end">
                <div class="banner-slogan">
                    <p>
                    Welcome to My {{ currentPhrase }}
                    </p>
                </div>
                <a
                    
                    class="banner-button btn rounded-pill btn-primary btn-lg px-4"
                    href="/about"
                    role="button"
                    >Discover More</a
                >
                </div>
            </div>
            </div>
        </div>
        </div>
    </div>

</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const phrases = [
  "Portfolio",
  "Website",
  "Domain",
];

const currentPhraseIndex = ref(0);
const currentCharacterIndex = ref(0);
const currentPhrase = ref("");
const isDeleting = ref(false);

/**
 * Animates typing and deleting effect for a list of phrases.
 *
 * This function simulates a typewriter effect by incrementally adding or removing characters
 * from the current phrase, updating the display accordingly. When a phrase is fully typed,
 * it waits for a buffer period before starting to delete. Once deleted, it moves to the next phrase.
 *
 * Variables used:
 * - phrases: Array of strings to display.
 * - currentPhraseIndex: Ref<number>, index of the current phrase.
 * - currentCharacterIndex: Ref<number>, index of the current character in the phrase.
 * - currentPhrase: Ref<string>, currently displayed phrase.
 * - isDeleting: Ref<boolean>, whether the function is deleting or typing.
 *
 * Timing:
 * - Typing speed is randomized between 100ms and 200ms per character.
 * - Deleting speed is randomized between 50ms and 80ms per character.
 * - After typing a phrase, waits 1200ms before deleting.
 *
 * The function calls itself recursively using setTimeout to continue the animation.
 */

function loop() {
  const currentPhraseText = phrases[currentPhraseIndex.value];

  if (!isDeleting.value) {
    currentPhrase.value += currentPhraseText[currentCharacterIndex.value];
    currentCharacterIndex.value++;
  } else {
    currentPhrase.value = currentPhrase.value.slice(0, -1);
    currentCharacterIndex.value--;
  }

  if (currentCharacterIndex.value === currentPhraseText.length) {
    isDeleting.value = true;
    setTimeout(loop, 1200); // buffer
    return

  }

  if (currentCharacterIndex.value === 0) {
    currentPhrase.value = "";
    isDeleting.value = false;
    currentPhraseIndex.value++;
    if (currentPhraseIndex.value === phrases.length) {
      currentPhraseIndex.value = 0;
    }
  }

  const spedUp = Math.random() * (80 - 50) + 50;
  const normalSpeed = Math.random() * (200 - 100) + 100;
  const time = isDeleting.value ? spedUp : normalSpeed;
  setTimeout(loop, time);
}

loop();



</script>