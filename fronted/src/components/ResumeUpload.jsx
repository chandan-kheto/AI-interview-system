
import { useState } from "react";
import API from "../services/api";


function ResumeUpload({ setInterviewData }) {

  const [resumeText, setResumeText] = useState("");

  const [role, setRole] = useState("AI/ML Engineer");

  const [loading, setLoading] = useState(false);

  const [uploading, setUploading] = useState(false);


  // Upload PDF Resume
  const uploadResume = async (e) => {

    const file = e.target.files[0];

    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    try {

      setUploading(true);

      const response = await API.post(
        "/upload-resume",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      // Auto-fill extracted resume text
      setResumeText(response.data.resume_text);

    } catch (error) {

      console.log(error);

      alert("Resume upload failed");

    } finally {

      setUploading(false);
    }
  };


  // Generate Interview
  const generateInterview = async () => {

    try {

      setLoading(true);

      const response = await API.post("/generate-interview", {
        resume_text: resumeText,
        role: role,
      });

      setInterviewData(response.data);

    } catch (error) {

      console.log(error);

      alert("Something went wrong");

    } finally {

      setLoading(false);
    }
  };


  return (

    <div className="bg-slate-800 rounded-xl">

      {/* Upload Resume */}
      <div className="mb-4">

        <label className="block px-2 mb-2 text-sm font-semibold">
          Upload Resume PDF
        </label>

        <input
          type="file"
          accept=".pdf"
          onChange={uploadResume}
          className="w-full p-3 text-sm rounded bg-slate-700 text-white"
        />

      </div>


      {/* Resume Text */}
      <textarea
        className="w-full p-4 text-sm rounded bg-slate-700 text-white"
        rows="6"
        placeholder="Paste Resume Text Here..."
        value={resumeText}
        onChange={(e) => setResumeText(e.target.value)}
      />


      {/* Role Selection */}
      <select
        className="w-full mt-3 text-sm p-3 rounded bg-slate-700 text-white"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      >
        <option>AI/ML Engineer</option>
        <option>Backend Engineer</option>
        <option>Data Scientist</option>
      </select>


      {/* Generate Button */}
      <button
        onClick={generateInterview}
        className="mt-5 w-full bg-blue-600 text-xs hover:bg-blue-700 px-4 py-3 rounded-lg"
      >

        {loading
          ? "Generating..."
          : uploading
          ? "Uploading Resume..."
          : "Generate Interview"}

      </button>

    </div>
  )
}

export default ResumeUpload