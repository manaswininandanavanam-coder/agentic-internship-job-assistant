import { useEffect, useState } from "react";
import "./App.css";
import {
  Upload,
  Search,
  FileText,
  Brain,
  Briefcase,
  Target,
  BookOpen,
  Send,
  BarChart3,
  Database,
  CheckCircle2,
  AlertCircle,
  Sparkles,
  MapPin,
  Building2,
  ExternalLink,
  ChevronDown,
  ChevronUp,
  X,
  Loader2,
  TrendingUp,
  GraduationCap,
  Zap,
} from "lucide-react";

const API_BASE = "https://agentic-internship-job-assistant-1.onrender.com";

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [resumeData, setResumeData] = useState(null);
  const [resumeText, setResumeText] = useState("");
  const [query, setQuery] = useState("AI/ML Intern");

  const [jobs, setJobs] = useState([]);
  const [selectedJob, setSelectedJob] = useState(null);

  const [analysis, setAnalysis] = useState(null);
  const [application, setApplication] = useState(null);
  const [applications, setApplications] = useState([]);
  const [applicationsLoading, setApplicationsLoading] = useState(false);

  const [loading, setLoading] = useState(false);
  const [analysisLoading, setAnalysisLoading] = useState(false);
  const [applicationLoading, setApplicationLoading] = useState(false);

  const [error, setError] = useState("");
  const [sortBy, setSortBy] = useState("match");
  {/* ================= AGENT WORKFLOW ================= */}

<section className="results-section">

  <div className="results-heading">
    <div>
      <div className="hero-badge">
        <Sparkles size={14} />
        Agentic AI Workflow
      </div>

      <h2>
        AI Agent Activity
      </h2>

      <p>
        Multiple AI agents work together to discover,
        analyze and manage internship opportunities.
      </p>
    </div>

    <div className="results-count">
      8 Agents
    </div>
  </div>

  <div className="agent-workflow-grid">

    <div className="agent-step completed">
      <div className="agent-icon">
        <FileText size={20} />
      </div>

      <div>
        <h3>Resume Agent</h3>
        <p>
          Extracts skills, education and experience
          from your resume.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Search size={20} />
      </div>

      <div>
        <h3>Job Discovery Agent</h3>
        <p>
          Searches internship opportunities based
          on your query.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Target size={20} />
      </div>

      <div>
        <h3>Matching Agent</h3>
        <p>
          Compares your skills with internship
          requirements.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <BarChart3 size={20} />
      </div>

      <div>
        <h3>Ranking Agent</h3>
        <p>
          Ranks internships according to
          compatibility.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Database size={20} />
      </div>

      <div>
        <h3>RAG Agent</h3>
        <p>
          Retrieves relevant information from
          your resume knowledge base.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Brain size={20} />
      </div>

      <div>
        <h3>Skill Gap Agent</h3>
        <p>
          Identifies missing skills and creates
          a learning roadmap.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Send size={20} />
      </div>

      <div>
        <h3>Application Agent</h3>
        <p>
          Generates application guidance,
          improvements and cover letters.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Briefcase size={20} />
      </div>

      <div>
        <h3>Tracking Agent</h3>
        <p>
          Stores and tracks your internship
          application status.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

  </div>

</section>
{/* ================= AGENT WORKFLOW ================= */}

<section className="results-section">

  <div className="results-heading">
    <div>
      <div className="hero-badge">
        <Sparkles size={14} />
        Agentic AI Workflow
      </div>

      <h2>
        AI Agent Activity
      </h2>

      <p>
        Multiple AI agents work together to discover,
        analyze and manage internship opportunities.
      </p>
    </div>

    <div className="results-count">
      8 Agents
    </div>
  </div>

  <div className="agent-workflow-grid">

    <div className="agent-step completed">
      <div className="agent-icon">
        <FileText size={20} />
      </div>

      <div>
        <h3>Resume Agent</h3>
        <p>
          Extracts skills, education and experience
          from your resume.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Search size={20} />
      </div>

      <div>
        <h3>Job Discovery Agent</h3>
        <p>
          Searches internship opportunities based
          on your query.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Target size={20} />
      </div>

      <div>
        <h3>Matching Agent</h3>
        <p>
          Compares your skills with internship
          requirements.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <BarChart3 size={20} />
      </div>

      <div>
        <h3>Ranking Agent</h3>
        <p>
          Ranks internships according to
          compatibility.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Database size={20} />
      </div>

      <div>
        <h3>RAG Agent</h3>
        <p>
          Retrieves relevant information from
          your resume knowledge base.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Brain size={20} />
      </div>

      <div>
        <h3>Skill Gap Agent</h3>
        <p>
          Identifies missing skills and creates
          a learning roadmap.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Send size={20} />
      </div>

      <div>
        <h3>Application Agent</h3>
        <p>
          Generates application guidance,
          improvements and cover letters.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

    <div className="agent-arrow">↓</div>

    <div className="agent-step completed">
      <div className="agent-icon">
        <Briefcase size={20} />
      </div>

      <div>
        <h3>Tracking Agent</h3>
        <p>
          Stores and tracks your internship
          application status.
        </p>
        <span>✓ Completed</span>
      </div>
    </div>

  </div>

</section>
    // ================= APPLICATION TRACKER =================

  const loadApplications = async () => {
    try {
      setApplicationsLoading(true);

      const response = await fetch(
        `${API_BASE}/api/applications`
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.error || "Failed to load applications."
        );
      }

      setApplications(data.applications || []);
    } catch (err) {
      console.error("Application tracker error:", err);
    } finally {
      setApplicationsLoading(false);
    }
  };

  useEffect(() => {
    loadApplications();
  }, []);

  const saveApplication = async (result) => {
    if (!result) return;

    const job = result.job || result;
    const match = result.match || {};

    try {
      const response = await fetch(
        `${API_BASE}/api/applications`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            job: job,
            match: match,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.error || "Failed to save application."
        );
      }

      await loadApplications();

      setError("");

      alert(
        "Application saved to your tracker successfully."
      );
    } catch (err) {
      console.error(err);

      setError(
        err.message ||
          "Failed to save application."
      );
    }
  };

  const updateApplicationStatus = async (
    applicationId,
    status
  ) => {
    try {
      const response = await fetch(
        `${API_BASE}/api/applications/${applicationId}/status`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            status: status,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.error ||
            "Failed to update application status."
        );
      }

      await loadApplications();
    } catch (err) {
      console.error(err);

      setError(
        err.message ||
          "Failed to update application status."
      );
    }
  };

  const deleteApplication = async (
    applicationId
  ) => {
    if (
      !window.confirm(
        "Remove this application from your tracker?"
      )
    ) {
      return;
    }

    try {
      const response = await fetch(
        `${API_BASE}/api/applications/${applicationId}`,
        {
          method: "DELETE",
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.error ||
            "Failed to delete application."
        );
      }

      await loadApplications();
    } catch (err) {
      console.error(err);

      setError(
        err.message ||
          "Failed to delete application."
      );
    }
  };
  const suggestions = [
    "AI/ML Intern",
    "Data Science Intern",
    "Python Developer Intern",
    "Software Developer Intern",
    "Web Development Intern",
  ];

  const handleResumeChange = (event) => {
    const file = event.target.files?.[0];

    if (!file) return;

    if (file.type !== "application/pdf") {
      setError("Please upload a PDF resume.");
      return;
    }

    setResumeFile(file);
    setError("");
    setResumeData(null);
    setResumeText("");
  };

  const handleFindInternships = async () => {
    setError("");
    setAnalysis(null);
    setApplication(null);
    setSelectedJob(null);

    if (!resumeFile) {
      setError("Please upload your resume first.");
      return;
    }

    if (!query.trim()) {
      setError("Please enter an internship search query.");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();

      formData.append("resume", resumeFile);
      formData.append("internship_query", query);

      const response = await fetch(
        `${API_BASE}/api/find-internships`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.error || "Failed to find internships."
        );
      }

      const agenticResults =
        data.agentic_results || {};

      const discoveredJobs =
        agenticResults.jobs || data.jobs || [];

      setJobs(discoveredJobs);
setResumeData(data.resume || data.resume_data || {});
setResumeText(data.resume_text || "");

      if (discoveredJobs.length === 0) {
        setError(
          "No internships were found for this search. Try another query."
        );
      }
    } catch (err) {
      console.error(err);

      setError(
        err.message ||
          "Unable to connect to the backend."
      );
    } finally {
      setLoading(false);
    }
  };

  const handleAnalyzeInternship = async (result) => {
    if (!result) return;

    setSelectedJob(result);
    setAnalysis(null);
    setApplication(null);
    setAnalysisLoading(true);
    setError("");

    try {
      const response = await fetch(
        `${API_BASE}/api/analyze-internship`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
              body: JSON.stringify({
  resume: resumeData || {},
  resume_data: resumeData || {},
  job: result.job || result,
  match: result.match || {},
  match_result: result.match || {},
}),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.error ||
            "Failed to analyze internship."
        );
      }

      setAnalysis(data);
    } catch (err) {
      console.error(err);

      setError(
        err.message ||
          "Failed to analyze this internship."
      );
    } finally {
      setAnalysisLoading(false);
    }
  };

  const handlePrepareApplication = async (result) => {
    if (!result) return;

    setSelectedJob(result);
    setApplication(null);
    setApplicationLoading(true);
    setError("");

    try {
      const response = await fetch(
        `${API_BASE}/api/prepare-application`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            resume_data: resumeData || {},
            job: result.job || result,
            match_result: result.match || {},
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.error ||
            "Failed to prepare application."
        );
      }

      setApplication(
        data.application || data
      );
    } catch (err) {
      console.error(err);

      setError(
        err.message ||
          "Failed to prepare application."
      );
    } finally {
      setApplicationLoading(false);
    }
  };

  const closeAnalysis = () => {
    setSelectedJob(null);
    setAnalysis(null);
    setApplication(null);
  };

  const getJobData = (result) => {
    return result?.job || result || {};
  };

  const getMatchData = (result) => {
    return result?.match || {};
  };

  const getScore = (result) => {
    const match = getMatchData(result);

    return Number(
      match.score ??
        result?.score ??
        0
    );
  };

  const getScoreClass = (score) => {
    if (score >= 70) return "strong";
    if (score >= 40) return "medium";
    return "low";
  };

  const sortedJobs = [...jobs].sort(
    (a, b) => {
      if (sortBy === "match") {
        return getScore(b) - getScore(a);
      }

      if (sortBy === "title") {
        return getJobData(a).title?.localeCompare(
          getJobData(b).title || ""
        );
      }

      return 0;
    }
  );

  const totalJobs = jobs.length;

  const averageScore =
    totalJobs > 0
      ? Math.round(
          jobs.reduce(
            (sum, job) =>
              sum + getScore(job),
            0
          ) / totalJobs
        )
      : 0;

  const topScore =
    totalJobs > 0
      ? Math.max(
          ...jobs.map((job) =>
            getScore(job)
          )
        )
      : 0;

  const resumeSkills =
    resumeData?.skills || [];

  return (
    <div className="app">
      {/* ================= TOP BAR ================= */}

      <header className="topbar">
        <div className="topbar-inner">
          <div className="brand">
            <div className="brand-mark">
              <Sparkles size={22} />
            </div>

            <div>
              <div className="brand-name">
                Internship AI
              </div>

              <div className="brand-subtitle">
                Agentic Career Assistant
              </div>
            </div>
          </div>

          <div className="topbar-status">
            <span className="status-dot"></span>
            AI Agents Online
          </div>
        </div>
      </header>

      {/* ================= MAIN ================= */}

      <main className="main-container">

        {/* ================= HERO ================= */}

        <section className="hero">
          <div className="hero-badge">
            <Zap size={15} />
            Powered by Agentic AI
          </div>

          <h1>
            Find internships that
            <span> match your skills.</span>
          </h1>

          <p>
            Upload your resume and let multiple AI
            agents discover, analyze, rank and prepare
            applications for real opportunities.
          </p>
        </section>

        {/* ================= SEARCH CARD ================= */}

        <section className="search-card">

          <div className="search-card-header">
            <div className="search-card-icon">
              <Search size={21} />
            </div>

            <div>
              <h2>
                Start your internship search
              </h2>

              <p>
                Upload your resume and describe
                the opportunity you're looking for.
              </p>
            </div>
          </div>

          <div className="form-grid">

            {/* RESUME */}

            <div className="form-group">
              <label>
                Resume
              </label>

              <label className="upload-box">
                <input
                  type="file"
                  accept=".pdf,application/pdf"
                  onChange={handleResumeChange}
                  hidden
                />

                <div className="upload-icon">
                  <Upload size={22} />
                </div>

                <div>
                  <strong>
                    {resumeFile
                      ? resumeFile.name
                      : "Upload your resume"}
                  </strong>

                  <span>
                    {resumeFile
                      ? "PDF selected"
                      : "PDF files only"}
                  </span>
                </div>
              </label>
            </div>

            {/* QUERY */}

            <div className="form-group">
              <label>
                Internship Search
              </label>

              <div className="query-input">
                <Search size={18} />

                <input
                  type="text"
                  value={query}
                  onChange={(e) =>
                    setQuery(e.target.value)
                  }
                  placeholder="e.g. AI/ML Intern"
                  onKeyDown={(e) => {
                    if (
                      e.key === "Enter"
                    ) {
                      handleFindInternships();
                    }
                  }}
                />
              </div>

              <div className="suggestion-row">
                {suggestions.map(
                  (suggestion) => (
                    <button
                      key={suggestion}
                      className="suggestion"
                      type="button"
                      onClick={() =>
                        setQuery(
                          suggestion
                        )
                      }
                    >
                      {suggestion}
                    </button>
                  )
                )}
              </div>
            </div>
          </div>

          <button
            className="search-button"
            type="button"
            onClick={
              handleFindInternships
            }
            disabled={loading}
          >
            {loading ? (
              <>
                <Loader2
                  size={18}
                  className="spin"
                />
                AI agents are searching...
              </>
            ) : (
              <>
                <Sparkles size={18} />
                Find Matching Internships
              </>
            )}
          </button>
        </section>

        {/* ================= AGENT STRIP ================= */}

        <section className="agent-strip">

          <AgentStatus
            icon={<FileText size={18} />}
            name="Resume Agent"
          />

          <AgentStatus
            icon={<Briefcase size={18} />}
            name="Job Discovery Agent"
          />

          <AgentStatus
            icon={<Target size={18} />}
            name="Matching Agent"
          />

          <AgentStatus
            icon={<BookOpen size={18} />}
            name="Skill Gap Agent"
          />

          <AgentStatus
            icon={<Send size={18} />}
            name="Application Agent"
          />

        </section>

        {/* ================= ERROR ================= */}

        {error && (
          <div className="error-message">
            <AlertCircle size={18} />
            <span>{error}</span>

            <button
              type="button"
              onClick={() =>
                setError("")
              }
            >
              <X size={16} />
            </button>
          </div>
        )}
        {/* ================= APPLICATION TRACKER ================= */}

<section className="results-section">

  <div className="results-heading">
    <div>
      <div className="hero-badge">
        <Briefcase size={14} />
        Application Tracker
      </div>

      <h2>
        My Applications
      </h2>

      <p>
        Track the internships you have saved and
        monitor your application progress.
      </p>
    </div>

    <div className="results-count">
      {applications.length} tracked
    </div>
  </div>

  {applicationsLoading ? (
    <div className="analysis-panel loading-panel">
      <Loader2
        size={22}
        className="spin"
      />

      <span>
        Loading your applications...
      </span>
    </div>
  ) : applications.length === 0 ? (
    <div className="empty-state">
      <div className="empty-state-icon">
        <Briefcase size={28} />
      </div>

      <h2>
        No applications tracked yet
      </h2>

      <p>
        Save an internship from your search results
        and it will appear here.
      </p>
    </div>
  ) : (
    <div className="jobs-container">

      {applications.map((item) => (

        <article
          className="job-card"
          key={item.id}
        >

          <div className="job-card-main">

            <div className="job-top">

              <div className="job-title-area">

                <div className="company-icon">
                  <Building2 size={20} />
                </div>

                <div>
                  <h3 className="job-title">
                    {item.job_title}
                  </h3>

                  <div className="company-name">
                    {item.company ||
                      "Company not specified"}
                  </div>
                </div>

              </div>

              <span className="opportunity-badge">
                {item.status}
              </span>

            </div>

            <div className="job-meta">

              <span>
                <MapPin size={15} />
                {item.location ||
                  "Location not specified"}
              </span>

              <span>
                <Target size={15} />
                {Number(
                  item.match_score || 0
                )}% Match
              </span>

            </div>

            <div className="match-details">

              <div className="match-detail-header">

                <div>
                  <strong>
                    Application Progress
                  </strong>

                  <span>
                    Update your current status
                  </span>
                </div>

                <span>
                  {item.status}
                </span>

              </div>

              <div
                style={{
                  display: "flex",
                  gap: "8px",
                  flexWrap: "wrap",
                  marginTop: "14px",
                }}
              >

                {[
                  "Saved",
                  "Applied",
                  "Interview",
                  "Selected",
                  "Rejected",
                ].map((status) => (

                  <button
                    key={status}
                    type="button"
                    className={
                      item.status === status
                        ? "apply-button"
                        : "analyze-button"
                    }
                    onClick={() =>
                      updateApplicationStatus(
                        item.id,
                        status
                      )
                    }
                  >
                    {status}
                  </button>

                ))}

              </div>

            </div>

          </div>

          <div className="job-footer">

            <div className="ai-ranked">
              <Sparkles size={14} />
              Application Tracking
            </div>

            <div className="job-actions">

              {item.apply_url && (
                <button
                  className="apply-button"
                  type="button"
                  onClick={() =>
                    window.open(
                      item.apply_url,
                      "_blank",
                      "noopener,noreferrer"
                    )
                  }
                >
                  <ExternalLink size={15} />
                  View & Apply
                </button>
              )}

              <button
                className="analyze-button"
                type="button"
                onClick={() =>
                  deleteApplication(item.id)
                }
              >
                <X size={15} />
                Remove
              </button>

            </div>

          </div>

        </article>

      ))}

    </div>
  )}

</section>

        {/* ================= RESUME ANALYSIS ================= */}

        {resumeData && (
          <section className="feature-grid">

            <div className="feature-card">
              <div className="feature-icon">
                <FileText size={20} />
              </div>

              <div>
                <h3>
                  Resume analyzed
                </h3>

                <p>
                  {resumeData.name ||
                    "Candidate"}
                </p>
              </div>

              <CheckCircle2
                size={20}
                className="success-icon"
              />
            </div>

            <div className="feature-card">
              <div className="feature-icon">
                <Brain size={20} />
              </div>

              <div>
                <h3>
                  AI skill extraction
                </h3>

                <p>
                  {resumeSkills.length} skills
                  detected
                </p>
              </div>

              <CheckCircle2
                size={20}
                className="success-icon"
              />
            </div>

            <div className="feature-card">
              <div className="feature-icon">
                <Briefcase size={20} />
              </div>

              <div>
                <h3>
                  Job discovery
                </h3>

                <p>
                  {totalJobs} opportunities
                  found
                </p>
              </div>

              {totalJobs > 0 && (
                <CheckCircle2
                  size={20}
                  className="success-icon"
                />
              )}
            </div>

          </section>
        )}

        {/* ================= RESULTS ================= */}

        {jobs.length > 0 && (
          <section className="results-section">

            <div className="results-heading">
              <div>
                <div className="hero-badge">
                  <Sparkles size={14} />
                  Agentic Results
                </div>

                <h2>
                  Real internship opportunities
                </h2>

                <p>
                  Ranked automatically using your
                  resume and required job skills.
                </p>
              </div>

              <div className="results-count">
                {totalJobs} opportunities
              </div>
            </div>

            {/* SUMMARY */}

            <div className="summary-grid">

              <div className="summary-card">
                <div className="summary-icon">
                  <Briefcase size={20} />
                </div>

                <div>
                  <span>
                    Opportunities
                  </span>

                  <strong>
                    {totalJobs}
                  </strong>
                </div>
              </div>

              <div className="summary-card">
                <div className="summary-icon">
                  <Target size={20} />
                </div>

                <div>
                  <span>
                    Average Match
                  </span>

                  <strong>
                    {averageScore}%
                  </strong>
                </div>
              </div>

              <div className="summary-card">
                <div className="summary-icon">
                  <TrendingUp size={20} />
                </div>

                <div>
                  <span>
                    Best Match
                  </span>

                  <strong>
                    {topScore}%
                  </strong>
                </div>
              </div>

            </div>

            {/* DETECTED SKILLS */}

            {resumeSkills.length > 0 && (
              <div className="detected-skills">
                <div>
                  <strong>
                    Detected resume skills
                  </strong>

                  <span>
                    Skills used by the Matching Agent
                  </span>
                </div>

                <div className="skills-columns">
                  {resumeSkills.map(
                    (skill, index) => (
                      <span
                        className="skill matched"
                        key={`${skill}-${index}`}
                      >
                        <CheckCircle2
                          size={13}
                        />
                        {skill}
                      </span>
                    )
                  )}
                </div>
              </div>
            )}

            {/* TOOLBAR */}

            <div className="results-toolbar">
              <div className="toolbar-title">
                <Sparkles size={17} />
                AI-ranked opportunities
              </div>

              <div className="toolbar-controls">
                <label className="control">
                  Sort by

                  <select
                    value={sortBy}
                    onChange={(e) =>
                      setSortBy(
                        e.target.value
                      )
                    }
                  >
                    <option value="match">
                      Match Score
                    </option>

                    <option value="title">
                      Job Title
                    </option>
                  </select>
                </label>
              </div>
            </div>

            {/* JOB CARDS */}

            <div className="jobs-container">

              {sortedJobs.map(
                (result, index) => (
                  <JobCard
                    key={
                      `${getJobData(result).title}-${index}`
                    }
                    result={result}
                    index={index}
                    onAnalyze={
                      handleAnalyzeInternship
                    }
                    onPrepareApplication={
                      handlePrepareApplication
                    }
                    onApply={() => {
                      const job =
                        getJobData(result);

                      if (
                        job.apply_url
                      ) {
                        window.open(
                          job.apply_url,
                          "_blank",
                          "noopener,noreferrer"
                        );
                      }
                    }}
                  />
                )
              )}

            </div>
          </section>
        )}

        {/* ================= ANALYSIS ================= */}

        {selectedJob && (
          <section className="analysis-section">

            <div className="analysis-heading">

              <div>
                <div className="hero-badge">
                  <Brain size={14} />
                  AI Career Analysis
                </div>

                <h2>
                  {getJobData(
                    selectedJob
                  ).title ||
                    "Internship Analysis"}
                </h2>

                <p>
                  Personalized analysis based on
                  your resume and this internship.
                </p>
              </div>

              <button
                className="close-analysis"
                type="button"
                onClick={
                  closeAnalysis
                }
              >
                <X size={18} />
              </button>

            </div>

            {/* ANALYSIS JOB HEADER */}

            <div className="analysis-job">

              <div className="analysis-company-icon">
                <Building2 size={22} />
              </div>

              <div>
                <strong>
                  {getJobData(
                    selectedJob
                  ).company ||
                    "Company"}
                </strong>

                <span>
                  <MapPin size={14} />

                  {getJobData(
                    selectedJob
                  ).location ||
                    "Hyderabad, Telangana"}
                </span>
              </div>

              <div
                className={`analysis-score ${getScoreClass(
                  getScore(
                    selectedJob
                  )
                )}`}
              >
                {getScore(
                  selectedJob
                )}%
                <small>
                  Match
                </small>
              </div>

            </div>

            {/* ANALYSIS STATS */}

            <div className="analysis-stats">

              <AnalysisStat
                icon={<Target size={19} />}
                value={
                  getMatchData(
                    selectedJob
                  ).matched_skills
                    ?.length || 0
                }
                label="Matched skills"
              />

              <AnalysisStat
                icon={<AlertCircle size={19} />}
                value={
                  getMatchData(
                    selectedJob
                  ).missing_skills
                    ?.length || 0
                }
                label="Skills to learn"
              />

              <AnalysisStat
                icon={<Briefcase size={19} />}
                value={
                  getMatchData(
                    selectedJob
                  ).required_skills
                    ?.length || 0
                }
                label="Required skills"
              />

            </div>

            {/* ANALYSIS BODY */}

            <div className="analysis-body">

              <div className="analysis-panel">

                <div className="match-detail-header">
                  <div>
                    <strong>
                      Skill matching
                    </strong>

                    <span>
                      How your resume compares
                      with the job
                    </span>
                  </div>

                  <span>
                    {getScore(
                      selectedJob
                    )}%
                  </span>
                </div>

                <div className="progress-track">
                  <div
                    className={`progress-fill ${getScoreClass(
                      getScore(
                        selectedJob
                      )
                    )}`}
                    style={{
                      width: `${Math.min(
                        100,
                        Math.max(
                          0,
                          getScore(
                            selectedJob
                          )
                        )
                      )}%`,
                    }}
                  />
                </div>

                <div className="skills-columns">

                  <div>
                    <h4>
                      <CheckCircle2
                        size={15}
                      />
                      Matched skills
                    </h4>

                    {(
                      getMatchData(
                        selectedJob
                      ).matched_skills ||
                      []
                    ).map(
                      (
                        skill,
                        index
                      ) => (
                        <div
                          className="skill matched"
                          key={`${skill}-${index}`}
                        >
                          <CheckCircle2
                            size={14}
                          />
                          {skill}
                        </div>
                      )
                    )}

                    {(
                      getMatchData(
                        selectedJob
                      ).matched_skills ||
                      []
                    ).length === 0 && (
                      <div className="empty-skill">
                        No matching skills detected.
                      </div>
                    )}
                  </div>

                  <div>
                    <h4>
                      <AlertCircle
                        size={15}
                      />
                      Missing skills
                    </h4>

                    {(
                      getMatchData(
                        selectedJob
                      ).missing_skills ||
                      []
                    ).map(
                      (
                        skill,
                        index
                      ) => (
                        <div
                          className="skill missing"
                          key={`${skill}-${index}`}
                        >
                          <AlertCircle
                            size={14}
                          />
                          {skill}
                        </div>
                      )
                    )}

                    {(
                      getMatchData(
                        selectedJob
                      ).missing_skills ||
                      []
                    ).length === 0 && (
                      <div className="empty-skill">
                        No major skill gaps detected.
                      </div>
                    )}
                  </div>

                </div>

              </div>

              {/* DESCRIPTION */}

              <div className="analysis-panel">

                <div className="match-detail-header">
                  <div>
                    <strong>
                      Internship details
                    </strong>

                    <span>
                      Opportunity information
                    </span>
                  </div>
                </div>

                <div className="job-description">
                  {getJobData(
                    selectedJob
                  ).description ? (
                    <p>
                      {stripHtml(
                        getJobData(
                          selectedJob
                        ).description
                      )}
                    </p>
                  ) : (
                    <p>
                      No detailed description
                      was provided by the job source.
                    </p>
                  )}
                </div>

              </div>

            </div>

            {/* ================= SKILL ROADMAP ================= */}

            {analysisLoading ? (
              <div className="analysis-panel loading-panel">
                <Loader2
                  size={24}
                  className="spin"
                />

                <span>
                  Skill Gap Agent is preparing
                  your personalized roadmap...
                </span>
              </div>
            ) : (
              analysis && (
                <SkillRoadmap
                  analysis={analysis}
                />
              )
            )}

            {/* ================= APPLICATION ================= */}

            {applicationLoading ? (
              <div className="analysis-panel loading-panel">
                <Loader2
                  size={24}
                  className="spin"
                />

                <span>
                  Application Agent is preparing
                  your application...
                </span>
              </div>
            ) : (
              application && (
                <ApplicationPanel
                  application={
                    application
                  }
                />
              )
            )}

            {/* ================= ACTIONS ================= */}

            <div className="job-footer">

              <div className="ai-ranked">
                <Sparkles size={15} />
                AI-powered career guidance
              </div>

              <div className="job-actions">

                {getJobData(
                  selectedJob
                ).apply_url && (
                  <button
                    className="apply-button"
                    type="button"
                    onClick={() =>
                      window.open(
                        getJobData(
                          selectedJob
                        ).apply_url,
                        "_blank",
                        "noopener,noreferrer"
                      )
                    }
                  >
                    <ExternalLink
                      size={16}
                    />
                    View & Apply
                  </button>
                )}

                <button
                  className="analyze-button"
                  type="button"
                  onClick={() =>
                    handlePrepareApplication(
                      selectedJob
                    )
                  }
                >
                  <Send size={16} />
                  Prepare Application
                </button>
                <button
  className="analyze-button"
  type="button"
  onClick={() =>
    saveApplication(selectedJob)
  }
>
  <Briefcase size={16} />
  Save Application
</button>

              </div>
            </div>

          </section>
        )}

        {/* ================= EMPTY STATE ================= */}

        {!loading &&
          jobs.length === 0 &&
          !resumeData && (
            <section className="empty-state">

              <div className="empty-state-icon">
                <GraduationCap size={30} />
              </div>

              <h2>
                Your AI career assistant is ready
              </h2>

              <p>
                Upload your resume, enter the type
                of internship you want, and let the
                AI agents handle the research.
              </p>

              <div className="empty-state-features">
                <span>
                  <CheckCircle2 size={15} />
                  Resume Analysis
                </span>

                <span>
                  <CheckCircle2 size={15} />
                  Real Job Discovery
                </span>

                <span>
                  <CheckCircle2 size={15} />
                  Smart Matching
                </span>

                <span>
                  <CheckCircle2 size={15} />
                  Skill Roadmap
                </span>
              </div>

            </section>
          )}

      </main>

      {/* ================= FOOTER ================= */}

      <footer className="footer">
        <div>
          <strong>
            Internship AI
          </strong>

          <span>
            Multi-Agent Career Intelligence Platform
          </span>
        </div>

        <span>
          Resume → Discover → Match → Learn → Apply
        </span>
      </footer>
    </div>
  );
}


/* =========================================================
   AGENT STATUS COMPONENT
========================================================= */

function AgentStatus({
  icon,
  name,
}) {
  return (
    <div className="agent-status">
      <div className="agent-status-icon">
        {icon}
      </div>

      <div>
        <strong>
          {name}
        </strong>

        <span>
          <span className="status-dot"></span>
          Online
        </span>
      </div>
    </div>
  );
}


/* =========================================================
   JOB CARD
========================================================= */

function JobCard({
  result,
  index,
  onAnalyze,
  onPrepareApplication,
  onApply,
}) {
  const job = result?.job || result || {};
  const match = result?.match || {};

  const score = Number(
    match.score ??
      result?.score ??
      0
  );

  const scoreClass =
    score >= 70
      ? "strong"
      : score >= 40
      ? "medium"
      : "low";

  const matchedSkills =
    match.matched_skills || [];

  const missingSkills =
    match.missing_skills || [];

  const description =
    stripHtml(
      job.description || ""
    );

  return (
    <article className="job-card">

      <div className="job-card-main">

        {/* TOP */}

        <div className="job-top">

          <div className="job-title-area">

            <div className="company-icon">
              <Building2 size={20} />
            </div>

            <div>
              <h3 className="job-title">
                {job.title ||
                  "Internship Opportunity"}
              </h3>

              <div className="company-name">
                {job.company ||
                  "Company not specified"}
              </div>
            </div>

          </div>

          <div className="job-badges">

            <span className="opportunity-badge">
              Internship
            </span>

            <span className="rank-badge">
              #{index + 1}
            </span>

          </div>

        </div>

        {/* MATCH SCORE */}

        <div className="match-circle-wrapper">

          <div
            className={`match-circle ${scoreClass}`}
          >
            <strong>
              {score}%
            </strong>

            <span>
              Match
            </span>
          </div>

        </div>

        {/* META */}

        <div className="job-meta">

          <span>
            <MapPin size={15} />

            {job.location ||
              "Hyderabad, Telangana"}
          </span>

          {job.contract_type && (
            <span>
              <Briefcase size={15} />
              {job.contract_type}
            </span>
          )}

          {job.salary_min && (
            <span>
              ₹{job.salary_min}
            </span>
          )}

        </div>

        {/* MATCH DETAILS */}

        <div className="match-details">

          <div className="match-detail-header">

            <div>
              <strong>
                Skill Match
              </strong>

              <span>
                {matchedSkills.length} matched
                {" • "}
                {missingSkills.length} missing
              </span>
            </div>

            <span>
              {score}%
            </span>

          </div>

          <div className="progress-track">

            <div
              className={`progress-fill ${scoreClass}`}
              style={{
                width: `${Math.min(
                  100,
                  Math.max(
                    0,
                    score
                  )
                )}%`,
              }}
            />

          </div>

          <div className="skills-columns">

            <div>
              <h4>
                <CheckCircle2
                  size={14}
                />
                Matched
              </h4>

              {matchedSkills.length >
              0 ? (
                matchedSkills
                  .slice(0, 8)
                  .map(
                    (
                      skill,
                      skillIndex
                    ) => (
                      <span
                        className="skill matched"
                        key={`${skill}-${skillIndex}`}
                      >
                        <CheckCircle2
                          size={12}
                        />
                        {skill}
                      </span>
                    )
                  )
              ) : (
                <span className="empty-skill">
                  No direct matches
                </span>
              )}
            </div>

            <div>
              <h4>
                <AlertCircle
                  size={14}
                />
                Missing
              </h4>

              {missingSkills.length >
              0 ? (
                missingSkills
                  .slice(0, 8)
                  .map(
                    (
                      skill,
                      skillIndex
                    ) => (
                      <span
                        className="skill missing"
                        key={`${skill}-${skillIndex}`}
                      >
                        <AlertCircle
                          size={12}
                        />
                        {skill}
                      </span>
                    )
                  )
              ) : (
                <span className="empty-skill">
                  No major gaps
                </span>
              )}
            </div>

          </div>

        </div>

        {/* DESCRIPTION */}

        {description && (
          <div className="job-description">
            <p>
              {description.length > 450
                ? `${description.slice(
                    0,
                    450
                  )}...`
                : description}
            </p>
          </div>
        )}

      </div>

      {/* FOOTER */}

      <div className="job-footer">

        <div className="ai-ranked">
          <Sparkles size={14} />
          AI Ranked
        </div>

        <div className="job-actions">

          <button
            className="analyze-button"
            type="button"
            onClick={() =>
              onAnalyze(result)
            }
          >
            <Brain size={15} />
            Analyze This Internship
          </button>

          <button
            className="analyze-button"
            type="button"
            onClick={() =>
              onPrepareApplication(
                result
              )
            }
          >
            <Send size={15} />
            Prepare Application
          </button>

          {job.apply_url && (
            <button
              className="apply-button"
              type="button"
              onClick={onApply}
            >
              <ExternalLink
                size={15}
              />
              View & Apply
            </button>
          )}

        </div>

      </div>

    </article>
  );
}


/* =========================================================
   ANALYSIS STAT
========================================================= */

function AnalysisStat({
  icon,
  value,
  label,
}) {
  return (
    <div className="analysis-stat">

      <div className="summary-icon">
        {icon}
      </div>

      <div>
        <strong>
          {value}
        </strong>

        <span>
          {label}
        </span>
      </div>

    </div>
  );
}


/* =========================================================
   SKILL ROADMAP
========================================================= */

function SkillRoadmap({
  analysis,
}) {
  const skillGaps =
    analysis?.skill_gaps ||
    analysis?.roadmap ||
    analysis?.gaps ||
    [];

  const matchScore =
    analysis?.match_score ??
    analysis?.score;

  if (
    !Array.isArray(skillGaps) ||
    skillGaps.length === 0
  ) {
    return (
      <div className="roadmap-section">

        <div className="roadmap-title">
          <div className="roadmap-icon">
            <BookOpen size={19} />
          </div>

          <div>
            <h3>
              Personalized Skill Roadmap
            </h3>

            <p>
              Your current profile was evaluated
              against the internship requirements.
            </p>
          </div>
        </div>

        <div className="no-gap-message">
          <CheckCircle2 size={20} />

          <div>
            <strong>
              No additional skill roadmap available
            </strong>

            <span>
              Your profile already covers the
              detected requirements, or the AI
              roadmap data was not returned.
            </span>
          </div>
        </div>

      </div>
    );
  }

  return (
    <div className="roadmap-section">

      <div className="roadmap-title">

        <div className="roadmap-icon">
          <BookOpen size={19} />
        </div>

        <div>
          <h3>
            Personalized Skill Roadmap
          </h3>

          <p>
            Learn the missing skills in a
            practical sequence.
            {matchScore !== undefined &&
              ` Current match: ${matchScore}%`}
          </p>
        </div>

      </div>

      <div className="roadmap-list">

        {skillGaps.map(
          (item, index) => {

            const skill =
              typeof item === "string"
                ? item
                : item.skill ||
                  item.name ||
                  item.title ||
                  `Skill ${index + 1}`;

            const importance =
              typeof item === "object"
                ? item.importance ||
                  item.priority ||
                  "Important"
                : "Important";

            const steps =
              typeof item === "object"
                ? item.learning_steps ||
                  item.steps ||
                  item.roadmap ||
                  []
                : [];

            return (
              <div
                className="roadmap-card"
                key={`${skill}-${index}`}
              >

                <div className="roadmap-number">
                  {index + 1}
                </div>

                <div className="roadmap-content">

                  <div className="roadmap-card-top">

                    <strong>
                      {skill}
                    </strong>

                    <span className="importance">
                      {importance}
                    </span>

                  </div>

                  {item.description && (
                    <p>
                      {item.description}
                    </p>
                  )}

                  {Array.isArray(
                    steps
                  ) &&
                    steps.length >
                      0 && (
                      <div className="learning-steps">

                        {steps.map(
                          (
                            step,
                            stepIndex
                          ) => (
                            <div
                              key={
                                stepIndex
                              }
                            >
                              <CheckCircle2
                                size={14}
                              />

                              <span>
                                {typeof step ===
                                "string"
                                  ? step
                                  : step.title ||
                                    step.description ||
                                    JSON.stringify(
                                      step
                                    )}
                              </span>
                            </div>
                          )
                        )}

                      </div>
                    )}

                </div>

              </div>
            );
          }
        )}

      </div>
    </div>
  );
}


/* =========================================================
   APPLICATION PANEL
========================================================= */

function ApplicationPanel({
  application,
}) {
  return (
    <div className="analysis-section application-result">

      <div className="analysis-heading">

        <div>
          <div className="hero-badge">
            <Send size={14} />
            Application Agent
          </div>

          <h2>
            Your application is ready
          </h2>

          <p>
            AI-generated application guidance
            based on your resume and the selected
            internship.
          </p>
        </div>

      </div>

      <div className="analysis-body">

        {/* FIT */}

        {application.why_you_are_a_good_fit && (
          <div className="analysis-panel">

            <div className="match-detail-header">
              <div>
                <strong>
                  Why you are a good fit
                </strong>

                <span>
                  Resume-aware recommendation
                </span>
              </div>
            </div>

            <div className="job-description">
              <p>
                {
                  application.why_you_are_a_good_fit
                }
              </p>
            </div>

          </div>
        )}

        {/* SKILLS */}

        <div className="analysis-panel">

          <div className="match-detail-header">
            <div>
              <strong>
                Skills to highlight
              </strong>

              <span>
                Mention these in your application
              </span>
            </div>
          </div>

          <div className="skills-columns">

            {(
              application.skills_to_highlight ||
              []
            ).map(
              (
                skill,
                index
              ) => (
                <span
                  className="skill matched"
                  key={`${skill}-${index}`}
                >
                  <CheckCircle2
                    size={13}
                  />
                  {skill}
                </span>
              )
            )}

          </div>

        </div>

        {/* RESUME IMPROVEMENTS */}

        {(
          application.resume_improvements ||
          []
        ).length > 0 && (
          <div className="analysis-panel">

            <div className="match-detail-header">
              <div>
                <strong>
                  Resume improvements
                </strong>

                <span>
                  Suggestions before applying
                </span>
              </div>
            </div>

            <div className="learning-steps">

              {application.resume_improvements.map(
                (
                  improvement,
                  index
                ) => (
                  <div
                    key={index}
                  >
                    <CheckCircle2
                      size={15}
                    />

                    <span>
                      {improvement}
                    </span>
                  </div>
                )
              )}

            </div>

          </div>
        )}

      </div>

      {/* COVER LETTER */}

      {application.cover_letter && (
        <div className="analysis-panel">

          <div className="match-detail-header">
            <div>
              <strong>
                AI-generated cover letter
              </strong>

              <span>
                Review and personalize before
                submitting
              </span>
            </div>
          </div>

          <div className="job-description">
            <p
              style={{
                whiteSpace:
                  "pre-line",
              }}
            >
              {
                application.cover_letter
              }
            </p>
          </div>

        </div>
      )}

      {/* CHECKLIST */}

      {(
        application.application_checklist ||
        []
      ).length > 0 && (
        <div className="analysis-panel">

          <div className="match-detail-header">
            <div>
              <strong>
                Application checklist
              </strong>

              <span>
                Complete these steps before
                submitting
              </span>
            </div>
          </div>

          <div className="learning-steps">

            {application.application_checklist.map(
              (
                item,
                index
              ) => (
                <div
                  key={index}
                >
                  <CheckCircle2
                    size={15}
                  />

                  <span>
                    {item}
                  </span>
                </div>
              )
            )}

          </div>

        </div>
      )}

    </div>
  );
}


/* =========================================================
   HTML CLEANER
========================================================= */

function stripHtml(text) {
  if (!text) return "";

  const temp =
    document.createElement(
      "div"
    );

  temp.innerHTML = text;

  return (
    temp.textContent ||
    temp.innerText ||
    ""
  )
    .replace(/\s+/g, " ")
    .trim();
}


export default App;