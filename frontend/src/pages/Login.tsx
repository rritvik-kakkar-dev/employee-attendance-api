import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

export default function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            const response = await api.post('/auth/login', {
                email: email,
                password: password
            });

            const token = response.data.access_token;
            if (token) {
                localStorage.setItem('access_token', token);
                navigate('/dashboard');
            }
        } catch (err: any) {
            setError(err.response?.data?.detail?.[0]?.msg || 'Login failed');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 px-4 sm:px-6 lg:px-8">
            {/* Main card - increased width on larger screens */}
            <div className="w-full max-w-md sm:max-w-lg md:max-w-xl lg:max-w-2xl bg-white/10 backdrop-blur-xl p-8 sm:p-10 md:p-12 rounded-3xl shadow-2xl border border-white/20">
                {/* Header */}
                <div className="text-center mb-10">
                    <h2 className="text-4xl md:text-5xl font-bold text-white tracking-tight">
                        Welcome Back
                    </h2>
                    <p className="mt-3 text-gray-300 text-lg">
                        Sign in to continue to your dashboard
                    </p>
                </div>

                {/* Error message */}
                {error && (
                    <div className="bg-red-500/30 border border-red-500 text-red-200 px-5 py-4 rounded-xl mb-8 text-center font-medium">
                        {error}
                    </div>
                )}

                {/* Form */}
                <form onSubmit={handleSubmit} className="space-y-7">
                    {/* Email */}
                    <div>
                        <label htmlFor="email" className="block text-sm font-medium text-gray-200 mb-2">
                            Email
                        </label>
                        <input
                            id="email"
                            type="email"
                            autoComplete="email"
                            required
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="w-full px-5 py-4 bg-white/10 border border-white/30 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:border-indigo-400 focus:ring-2 focus:ring-indigo-500/40 transition-all duration-200"
                            placeholder="you@example.com"
                        />
                    </div>

                    {/* Password */}
                    <div>
                        <label htmlFor="password" className="block text-sm font-medium text-gray-200 mb-2">
                            Password
                        </label>
                        <input
                            id="password"
                            type="password"
                            autoComplete="current-password"
                            required
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full px-5 py-4 bg-white/10 border border-white/30 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:border-indigo-400 focus:ring-2 focus:ring-indigo-500/40 transition-all duration-200"
                            placeholder="••••••••••••"
                        />
                    </div>

                    {/* Submit button */}
                    <button
                        type="submit"
                        disabled={loading}
                        className={`w-full py-4 px-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold text-lg rounded-xl shadow-lg focus:outline-none focus:ring-4 focus:ring-indigo-500/50 transition-all duration-200 ${loading ? 'opacity-70 cursor-not-allowed' : ''
                            }`}
                    >
                        {loading ? (
                            <span className="flex items-center justify-center">
                                <svg className="animate-spin h-5 w-5 mr-3 text-white" viewBox="0 0 24 24">
                                    <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                                </svg>
                                Logging in...
                            </span>
                        ) : (
                            'Sign In'
                        )}
                    </button>
                </form>

                {/* Register link */}
                <p className="mt-8 text-center text-gray-300">
                    Don't have an account?{' '}
                    <a
                        href="/register"
                        className="text-indigo-400 hover:text-indigo-300 font-medium transition-colors"
                    >
                        Register here
                    </a>
                </p>
            </div>
        </div>
    );
}