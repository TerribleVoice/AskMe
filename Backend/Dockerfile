FROM mcr.microsoft.com/dotnet/sdk:6.0 as build
WORKDIR /src
COPY AskMe.sln .
COPY AskMe.WebApi/*.csproj ./AskMe.WebApi/
COPY AskMe.Core/*.csproj ./AskMe.Core/
COPY AskMe.Service/*.csproj ./AskMe.Service/
RUN dotnet restore
COPY . .

WORKDIR /src/AskMe.WebApi
RUN dotnet build -c Debug -o /publish

WORKDIR /src
RUN dotnet build -c Debug -o /publish

WORKDIR /src/AskMe.Service
RUN dotnet build -c Debug -o /publish


FROM build as publish
WORKDIR /src
RUN dotnet publish -c Debug -o /publish

FROM mcr.microsoft.com/dotnet/aspnet:6.0 as final
WORKDIR /publish
COPY --from=publish /publish .
EXPOSE 80

ENTRYPOINT ["dotnet", "AskMe.WebApi.dll"]
