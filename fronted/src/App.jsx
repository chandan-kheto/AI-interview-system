
import { useState } from "react";

import ResumeUpload from "./components/ResumeUpload";
import AnswerSection from "./components/AnswerSection";


function App() {

  const [interviewData, setInterviewData] = useState(null);

  return (

    <div className="min-h-screen bg-slate-900 text-white py-5 px-20">

      <h1 className="text-3xl font-bold text-center mb-10">
       🤖 AI Interview System
      </h1>

      <ResumeUpload setInterviewData={setInterviewData} />

      {interviewData && (

        <div className="bg-slate-800 p-6 rounded-xl mt-6">

          <h2 className="text-sm font-bold mb-4">
            Generated Questions
          </h2>

          <div className="whitespace-pre-wrap text-slate-200 leading-8 text-[14px]">
            {interviewData.questions}
          </div>

        </div>
      )}

      {/* Answer + Evaluation */}
      {interviewData && (

        <AnswerSection
          sessionId={interviewData.session_id}
        />
      )}

    </div>
  )
}

export default App