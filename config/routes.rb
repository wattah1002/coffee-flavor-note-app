Rails.application.routes.draw do
  get 'static_pages/home'
  # get 'users/new'
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html
  get '/signup', to: 'users#new'
  # Defines the root path route ("/")
  # root "articles#index"
end
