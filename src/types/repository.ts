export type Repository = {
  name: string;
  owner: string;
  description: string;
  stars: number;
  forks: number;
  language: string;
  languages: string[];
  avatar: string;
  html_url: string;
  updated_at: string;
  analysis: {
    summary: string;
    strengths: string[];
    improvements: string[];
    score: number;
  };
};