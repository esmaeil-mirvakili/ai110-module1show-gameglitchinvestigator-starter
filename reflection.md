# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Pressing enter doesn't submit the guess
- The messages "Go Higher" and "Go Lower" are actually opposite.
- The developer debug info doesn't get updated as we submit the guess.
- When I start a new game, the score is not reset in the developer info.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  We used Claude code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Claude Code correctly suggested putting the input and submit button inside a `st.form` so pressing Enter would submit the guess. I verified it by running the app and confirming Enter worked the same as clicking the button.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Claude Code first moved the developer debug info lower on the page to make it update correctly, but that changed the layout in a way I did not want. I verified it by running the app, then we fixed it by using a `st.empty()` placeholder so the info stayed at the top and still updated.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I checked each bug by running the app and making sure the behavior changed in the way I expected. If the game still acted strangely after a change, I kept debugging.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran `pytest` on `tests/test_game_logic.py` and all 17 tests passed. That showed the main game logic, like hints, score updates, and difficulty ranges, was working correctly.
- Did AI help you design or understand any tests? How?
  Yes. Claude Code helped write the tests for the logic functions and connected them to the bugs we had already fixed in the app.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  The secret number kept changing because Streamlit reruns the script after each interaction. If the value is not stored in `st.session_state`, it gets recreated again.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would say Streamlit reloads your script from top to bottom every time the user clicks something. `st.session_state` is how you keep values between those reruns.
- What change did you make that finally gave the game a stable secret number?
  I kept the secret number inside `st.session_state` and only created it if it was not already there. That stopped it from changing every time the app reran.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to keep writing tests after fixing bugs so I can check that the same problem does not come back.
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time I would verify each AI suggestion sooner instead of assuming the first fix was enough.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me that AI-generated code can be useful, but it still needs careful testing and review. I now trust AI more as a helper than as something I should blindly accept.
