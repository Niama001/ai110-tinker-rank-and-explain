"""
Target file for Tinker 1B, Part 2.

Move `apply_streak_bonus(combined_score, streak_days)` here from scoring.py,
then update the import at the top of scoring.py so `run_demo()` and the
Session Scorer tab still work exactly as before.
"""

# TODO: move apply_streak_bonus(combined_score, streak_days) here from scoring.py
from scoring_helpers import apply_streak_bonus


def session_rating(combined_score: int) -> str:
    """Rate a study session from its combined minutes+focus score. Correct and tested."""
    if combined_score >= 90:
        return "Great"
    if combined_score >= 80:
        return "Good"
    if combined_score >= 70:
        return "OK"
    if combined_score >= 60:
        return "Meh"
    return "Skip"


def render_session_scorer_tab():
    import streamlit as st

    st.subheader("Score a Session")
    minutes = st.slider("Minutes studied", 0, 60, 30)
    focus = st.slider("Focus (0-60)", 0, 60, 30)
    streak = st.number_input("Current streak (days)", min_value=0, value=0, step=1)

    combined = minutes + focus
    boosted = apply_streak_bonus(combined, streak)
    rating = session_rating(boosted)
    st.metric("Rating", rating, help=f"Combined {combined} -> boosted {boosted}")


def run_demo():
    sessions = [55, 68, 82, 91, 77]
    streak = 3
    for raw in sessions:
        boosted = apply_streak_bonus(raw, streak)
        rating = session_rating(boosted)
        print(f"Raw: {raw} -> Boosted: {boosted} -> Rating: {rating}")


if __name__ == "__main__":
    run_demo()