import React, { useState } from 'react';
import "./index.css";

const Cricket = (props) => {
    const [runs, setRuns] = useState(0);
    const [wickets, setWickets] = useState(0);
    const [balls, setBalls] = useState(0);
    const [currentOvers, setCurrentOvers] = useState(0);
    const [remainingOvers, setRemainingOvers] = useState(20);
    const target = props.target;

    const handleBall = (run) => {
        if (runs + run >= 200) {
            alert("🎯 Target Chased!");
        }
         if (run === 6) {
        alert("6️⃣ Six hit!");
    } else if (run === 4) {
        alert("4️⃣ Four hit!");
    }

        setRuns(prev => prev + run);
        updateBallCount();
    };

    const updateBallCount = () => {
        setBalls(prevBalls => {
            if (prevBalls === 5) {
                setCurrentOvers(prev => prev + 1);
                setRemainingOvers(prev => prev - 1);
                return 0;
            } else {
                return prevBalls + 1;
            }
        });
    };

    const handleWicket = () => {
        alert("🏏 Wicket taken!");
        if (wickets + 1 === 10) {
            alert("💥 All out");
        }
        setWickets(prev => prev + 1);
        updateBallCount();
    };

    const gameOver = wickets >= 10 || runs >= target || remainingOvers <= 0;

    return (
        <>
            <h1>Score: {runs}/{wickets}</h1>
            <h3>Current Over: {currentOvers}.{balls}</h3>
            <h3>Remaining Overs: {remainingOvers}</h3>

            {!gameOver ? (
                <div>
                    <button onClick={() => handleBall(6)}>Six</button>
                    <button onClick={() => handleBall(4)}>Four</button>
                    <button onClick={() => handleBall(3)}>Three</button>
                    <button onClick={() => handleBall(2)}>Two</button>
                    <button onClick={() => handleBall(1)}>One</button>
                    <button onClick={() => handleBall(0)}>Dot</button>
                    <button onClick={handleWicket}>Wicket</button>
                </div>
            ) : (
                <h3>🏁 Game Over</h3>
            )}
        </>
    );
};

export default Cricket;
