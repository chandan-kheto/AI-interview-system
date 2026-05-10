
import { useState } from "react";

import API from "../services/api";


function AnswerSection({ sessionId }) {

  const [answer, setAnswer] = useState("");

  const [evaluation, setEvaluation] = useState("");

  const [loading, setLoading] = useState(false);


  // Submit Answer
  const submitAnswer = async () => {

    try {

      await API.post("/submit-answer", {
        session_id: sessionId,
        answer: answer,
      });

      alert("Answer submitted successfully!");

      setAnswer("");

    } catch (error) {

      console.log(error);

      alert("Failed to submit answer");
    }
  };


  // Evaluate Interview
  const evaluateInterview = async () => {

    try {

      setLoading(true);

      const response = await API.get(
        `/evaluate/${sessionId}`
      );

      setEvaluation(response.data.evaluation);

    } catch (error) {

      console.log(error);

      alert("Evaluation failed");

    } finally {

      setLoading(false);
    }
  };


  return (

    <div className="max-w-7xl mx-auto bg-slate-800 p-6 rounded-2xl mt-8 shadow-lg">

      <h2 className="text-sm font-bold mb-3">
        Submit Your Answer
      </h2>


      {/* Answer Input */}
      <textarea
        className="w-full p-4 text-sm rounded-xl bg-slate-700 text-white border border-slate-600"
        rows="5"
        placeholder="Write your interview answer here..."
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
      />


      {/* Buttons */}
      <div className="grid grid-cols-2 flex gap-4 mt-5">

        <button
          onClick={submitAnswer}
          className="bg-green-600 text-sm hover:bg-green-700 px py-3 rounded-xl font-semibold"
        >
          Submit Answer
        </button>


        <button
          onClick={evaluateInterview}
          className="bg-purple-600 text-sm hover:bg-purple-700 px- py-3 rounded-xl font-semibold"
        >

          {loading
            ? "Evaluating..."
            : "Evaluate Interview"}

        </button>

      </div>


      {/* Evaluation Result */}
      {evaluation && (

        <div className="bg-slate-700 p-5 rounded-xl mt-8">

          <h3 className="text-2xl font-bold mb-4">
            AI Evaluation
          </h3>

          <div className="whitespace-pre-wrap leading-8 text-slate-200">

            {evaluation}

          </div>

        </div>
      )}

    </div>
  )
}

export default AnswerSection