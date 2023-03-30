﻿using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using PracticeApplication.WebSite.Services;
using PracticeApplication.WebSite.Models;

namespace PracticeApplication.WebSite.Controllers
{
	[Route("[controller]")]
	[ApiController]
	public class ProductsController : ControllerBase
	{
		public ProductsController(JsonFileProductService productService) {
			this.ProductService = productService;
		}

		public JsonFileProductService ProductService { get; }

		[HttpGet]
		public IEnumerable<Product> get()
		{
			return ProductService.GetProducts();
		}
	}
}
